#!/usr/bin/env bash
set -uo pipefail

IMAGE_NAME="ue-rag-assistant"
CONTAINER_NAME="ue-rag-assistant"
DOCKERFILE="Dockerfile"
ENV_FILE="${ENV_FILE:-.env}"

PORT="${PORT:-7860}"
DOCKER_MEMORY="${DOCKER_MEMORY:-4g}"

if ! command -v docker >/dev/null 2>&1; then
  echo "docker CLI not found. Install Docker Desktop or fix your PATH."
  exit 1
fi

if ! docker version >/dev/null 2>&1; then
  echo "Docker daemon not reachable. Start Docker Desktop and try again."
  exit 1
fi

if [[ ! -f "${ENV_FILE}" ]]; then
  echo "Env file not found: ${ENV_FILE}"
  exit 1
fi

echo "Stopping/removing container (if it exists): ${CONTAINER_NAME}"
docker rm -f "${CONTAINER_NAME}" >/dev/null 2>&1 || true

echo "Rebuilding Docker image: ${IMAGE_NAME}"
docker build -t "${IMAGE_NAME}" -f "${DOCKERFILE}" .

echo "Starting container (memory limit: ${DOCKER_MEMORY})..."

RUN_ARGS=(
  --name "${CONTAINER_NAME}"
  --memory "${DOCKER_MEMORY}"
  -p "${PORT}:7860"
  -v "$(pwd):/app"
  --env-file "${ENV_FILE}"
  -e "PORT=${PORT}"
  -e "FORCE_REBUILD_VECTORSTORE=${FORCE_REBUILD_VECTORSTORE:-0}"
)

docker run "${RUN_ARGS[@]}" "${IMAGE_NAME}"
EXIT_CODE=$?

if [[ ${EXIT_CODE} -eq 0 ]]; then
  echo "Container stopped normally."
  docker rm -f "${CONTAINER_NAME}" >/dev/null 2>&1 || true
  exit 0
fi

OOM_KILLED="false"
INSPECT_JSON=$(docker inspect "${CONTAINER_NAME}" 2>/dev/null) && \
  OOM_KILLED=$(echo "${INSPECT_JSON}" | python3 -c "import sys,json; print(json.load(sys.stdin)[0]['State']['OOMKilled'])" 2>/dev/null || echo "false")

if [[ "${OOM_KILLED}" == "True" ]] || [[ ${EXIT_CODE} -eq 137 ]]; then
  echo ""
  echo "============================================"
  echo "  OOM DETECTED (exit code ${EXIT_CODE})"
  echo "============================================"
  echo "The container ran out of memory."
  echo ""
  echo "Options:"
  echo "  1. Increase memory limit:  DOCKER_MEMORY=6g ./restart_rag_docker.sh"
  echo "  2. Reduce chunk count:     Add VSTORE_MAX_CHUNKS=4000 to .env"
  echo "  3. Use sharded strategy (default): VSTORE_SHARD_STRATEGY=sharded_by_path_level_1"
  echo ""
  echo "Killing and removing the OOM-killed container..."
  docker rm -f "${CONTAINER_NAME}" >/dev/null 2>&1 || true
  exit 137
fi

echo "Container exited with code ${EXIT_CODE}."
docker rm -f "${CONTAINER_NAME}" >/dev/null 2>&1 || true
exit ${EXIT_CODE}
