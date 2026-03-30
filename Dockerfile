FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV GRADIO_SERVER_NAME=0.0.0.0
ENV PORT=7860

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements_rag.txt /app/requirements_rag.txt
RUN pip install --no-cache-dir -r /app/requirements_rag.txt

COPY rag_assistant /app/rag_assistant

# The container expects scraped_data/ and unreal_specifiers/ to be present at /app/
# (recommended: mount your repo into the container instead of copying scraped_data).

EXPOSE 7860

CMD ["python", "-m", "rag_assistant.app"]

