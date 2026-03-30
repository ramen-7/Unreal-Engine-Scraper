# Paste of notebook cell 3 — also run: python -c "import json, pathlib; ..." to sync into .ipynb
import asyncio
import json
import random
import re
import time
from pathlib import Path

from bs4 import BeautifulSoup
from markdownify import markdownify as html_to_md
from playwright.async_api import async_playwright
from tqdm import tqdm

HERE = Path(".").resolve()
URLS_JSON = HERE / "scraped_data" / "urls" / "full_ur_with_paths.json"
OUTPUT_ROOT = HERE / "scraped_data" / "markdown_by_path"
PROGRESS_PATH = HERE / "scraped_data" / "markdown_scrape" / "progress.jsonl"

# --- Browser session ---
# "bundled" — Playwright Chromium (often throttled)
# "cdp" — attach to YOUR Chrome (quit Chrome first, then):
#   macOS: /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
# "storage_state" — JSON from await context.storage_state(path="...")
BROWSER_MODE = "bundled"  # "bundled" | "cdp" | "storage_state"
CDP_URL = "http://127.0.0.1:9222"
STORAGE_STATE_PATH: Path | None = None

# Extra headers (minor); real session = use CDP. Example:
# EXTRA_HTTP_HEADERS = {"Accept-Language": "en-US,en;q=0.9"}
EXTRA_HTTP_HEADERS: dict[str, str] = {}

DELAY_S = 4.0
DELAY_JITTER = (0.5, 2.5)

NAV_TIMEOUT_MS = 120_000
SELECTOR_TIMEOUT_MS = 90_000
DOC_ROOT_SELECTOR = "main, [role='main'], article, .documentation-content"

MAIN_READY_MIN_CHARS = 150
MAIN_READY_TRUST_LEN = 450
DOC_POLL_MS = 500
DOC_POLL_MAX_ROUNDS = 120

MAX_RETRIES = 3
RETRY_BACKOFF_BASE_S = 3
MAX_CONSECUTIVE_ERRORS = 3
BROWSER_RESTART_COOLDOWN_S = 10

PAUSE_AFTER_FIRST_OK_S = 18.0
CLEAR_COOKIES_BETWEEN_NAVIGATIONS = True
NEW_PAGE_PER_URL = True

MAX_PAGES = None
START_INDEX = 0
END_INDEX = None

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)

_MULTI_UNDERSCORE = re.compile(r"_+")
_FORBIDDEN_FILENAME_CHARS = frozenset('<>:"/\\|?*')


def sanitize_filename(name: str, max_len: int = 180) -> str:
    out: list[str] = []
    for ch in name.strip():
        if ord(ch) < 32 or ch in _FORBIDDEN_FILENAME_CHARS:
            out.append("_")
        else:
            out.append(ch)
    s = _MULTI_UNDERSCORE.sub("_", "".join(out)).strip("._ ")
    if not s:
        s = "untitled"
    return s[:max_len]


def output_dir_for_entry(entry: dict, out_root: Path) -> Path:
    segs = entry.get("path_segments") or []
    parent_parts = [sanitize_filename(s) for s in segs[:-1]] if len(segs) > 1 else []
    return out_root.joinpath(*parent_parts) if parent_parts else out_root


def unique_output_path(rel_dir: Path, title: str) -> Path:
    rel_dir.mkdir(parents=True, exist_ok=True)
    stem = sanitize_filename(title)
    p = rel_dir / f"{stem}.md"
    if not p.exists():
        return p
    n = 2
    while True:
        cand = rel_dir / f"{stem}_{n}.md"
        if not cand.exists():
            return cand
        n += 1


def doc_root_from_soup(soup: BeautifulSoup):
    return (
        soup.find("main")
        or soup.select_one("[role='main']")
        or soup.select_one("article")
        or soup.select_one(".documentation-content")
    )


def main_inner_text_len(html: str) -> int:
    soup = BeautifulSoup(html, "lxml")
    m = doc_root_from_soup(soup)
    return len((m.get_text() or "").strip()) if m else 0


def body_has_is_page_error(html: str) -> bool:
    soup = BeautifulSoup(html, "lxml")
    body = soup.find("body")
    cls = body.get("class") if body else []
    return bool(cls and "is-page-error" in cls)


async def wait_for_any_content(page) -> None:
    try:
        await page.wait_for_selector(
            DOC_ROOT_SELECTOR,
            state="attached",
            timeout=SELECTOR_TIMEOUT_MS,
        )
    except Exception:
        try:
            await page.wait_for_load_state("networkidle", timeout=SELECTOR_TIMEOUT_MS)
        except Exception:
            pass


async def wait_for_documentation_html(page, url: str, referer: str | None) -> str:
    goto_kw: dict = {"wait_until": "load", "timeout": NAV_TIMEOUT_MS}
    if referer:
        goto_kw["referer"] = referer
    await page.goto(url, **goto_kw)
    await wait_for_any_content(page)
    for _ in range(DOC_POLL_MAX_ROUNDS):
        html = await page.content()
        n = main_inner_text_len(html)
        err = body_has_is_page_error(html)
        if n >= MAIN_READY_MIN_CHARS and not err:
            return html
        if n >= MAIN_READY_TRUST_LEN:
            return html
        await page.wait_for_timeout(DOC_POLL_MS)
    raise RuntimeError(
        "documentation did not become ready; try BROWSER_MODE='cdp', or increase waits"
    )


def load_done_urls(progress_path: Path) -> set[str]:
    done: set[str] = set()
    if not progress_path.exists():
        return done
    with open(progress_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
                if row.get("status") == "ok" and row.get("scrape_url"):
                    done.add(row["scrape_url"])
            except json.JSONDecodeError:
                continue
    return done


def append_progress(progress_path: Path, record: dict) -> None:
    progress_path.parent.mkdir(parents=True, exist_ok=True)
    with open(progress_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def extract_main_html(page_html: str) -> str | None:
    soup = BeautifulSoup(page_html, "lxml")
    root = doc_root_from_soup(soup)
    if not root:
        return None
    return str(root)


def page_to_markdown(page_html: str, title: str, scrape_url: str) -> str:
    inner = extract_main_html(page_html)
    if inner is None:
        return ""
    body_md = html_to_md(inner, heading_style="ATX")
    header = f"<!-- source: {scrape_url} -->\n\n# {title}\n\n"
    return header + body_md.strip() + "\n"


def _context_options() -> dict:
    o: dict = {
        "user_agent": USER_AGENT,
        "viewport": {"width": 1280, "height": 800},
        "locale": "en-US",
    }
    if BROWSER_MODE == "storage_state" and STORAGE_STATE_PATH:
        p = Path(STORAGE_STATE_PATH)
        if p.is_file():
            o["storage_state"] = str(p)
    if EXTRA_HTTP_HEADERS:
        o["extra_http_headers"] = EXTRA_HTTP_HEADERS
    return o


async def new_browser_session(p, *, connect_cdp: bool):
    if connect_cdp:
        browser = await p.chromium.connect_over_cdp(CDP_URL)
        contexts = browser.contexts
        if not contexts:
            context = await browser.new_context(**_context_options())
        else:
            context = contexts[0]
        page = await context.new_page()
        if EXTRA_HTTP_HEADERS:
            await context.set_extra_http_headers(EXTRA_HTTP_HEADERS)
        return browser, context, page, True
    browser = await p.chromium.launch(
        headless=True,
        args=["--disable-blink-features=AutomationControlled"],
    )
    context = await browser.new_context(**_context_options())
    page = await context.new_page()
    return browser, context, page, False


async def sleep_between_requests() -> None:
    await asyncio.sleep(DELAY_S + random.uniform(DELAY_JITTER[0], DELAY_JITTER[1]))


async def doc_page_for_url(context, page, last_url: str | None):
    if not NEW_PAGE_PER_URL:
        return page
    if last_url is None:
        return page
    await page.close()
    return await context.new_page()


async def scrape_all() -> None:
    entries = json.loads(URLS_JSON.read_text(encoding="utf-8"))
    if END_INDEX is not None:
        entries = entries[START_INDEX:END_INDEX]
    else:
        entries = entries[START_INDEX:]
    if MAX_PAGES is not None:
        entries = entries[:MAX_PAGES]

    done_urls = load_done_urls(PROGRESS_PATH)
    todo = [e for e in entries if e.get("scrape_url") and e["scrape_url"] not in done_urls]
    print(f"Total in slice: {len(entries)}, already OK in log: {len(done_urls)}, to fetch: {len(todo)}")
    print(f"BROWSER_MODE={BROWSER_MODE!r}")

    if BROWSER_MODE == "storage_state" and (
        not STORAGE_STATE_PATH or not Path(STORAGE_STATE_PATH).is_file()
    ):
        raise FileNotFoundError("Set STORAGE_STATE_PATH to a storage_state JSON file")

    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

    connect_cdp = BROWSER_MODE == "cdp"

    async with async_playwright() as p:
        browser, context, page_ref, cdp_attached = await new_browser_session(
            p, connect_cdp=connect_cdp
        )
        last_url: str | None = None
        consecutive_errors = 0
        ok_count = 0

        clear_cookies_each = CLEAR_COOKIES_BETWEEN_NAVIGATIONS and BROWSER_MODE != "cdp"

        for entry in tqdm(todo, desc="Pages"):
            url = entry["scrape_url"]
            title = entry.get("title") or "untitled"
            rel_dir = output_dir_for_entry(entry, OUTPUT_ROOT)
            out_path = unique_output_path(rel_dir, title)
            t0 = time.perf_counter()
            if clear_cookies_each and last_url is not None:
                await context.clear_cookies()
            page_ref = await doc_page_for_url(context, page_ref, last_url)
            ok = False
            last_err: Exception | None = None
            for attempt in range(MAX_RETRIES):
                try:
                    html = await wait_for_documentation_html(page_ref, url, last_url)
                    md = page_to_markdown(html, title, url)
                    if not md or len(md) < 80:
                        raise RuntimeError("empty or very short markdown")
                    out_path.parent.mkdir(parents=True, exist_ok=True)
                    out_path.write_text(md, encoding="utf-8")
                    append_progress(
                        PROGRESS_PATH,
                        {
                            "status": "ok",
                            "scrape_url": url,
                            "path": str(out_path.relative_to(HERE)),
                            "elapsed_s": round(time.perf_counter() - t0, 3),
                        },
                    )
                    last_url = url
                    consecutive_errors = 0
                    ok = True
                    ok_count += 1
                    if ok_count == 1:
                        await asyncio.sleep(PAUSE_AFTER_FIRST_OK_S)
                    break
                except Exception as e:
                    last_err = e
                    if attempt < MAX_RETRIES - 1:
                        await asyncio.sleep((2**attempt) * RETRY_BACKOFF_BASE_S)
            if not ok:
                append_progress(
                    PROGRESS_PATH,
                    {
                        "status": "error",
                        "scrape_url": url,
                        "error": str(last_err) if last_err else "unknown",
                        "elapsed_s": round(time.perf_counter() - t0, 3),
                    },
                )
                consecutive_errors += 1
                if consecutive_errors >= MAX_CONSECUTIVE_ERRORS:
                    await browser.close()
                    browser, context, page_ref, cdp_attached = await new_browser_session(
                        p, connect_cdp=connect_cdp
                    )
                    consecutive_errors = 0
                    await asyncio.sleep(BROWSER_RESTART_COOLDOWN_S)
            await sleep_between_requests()

        await browser.close()

    print("Done.")


if __name__ == "__main__":
    asyncio.run(scrape_all())
