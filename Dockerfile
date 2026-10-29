# syntax=docker/dockerfile:1
# Stage 1: build frontend assets; Node tooling is excluded from runtime.
FROM node:22-alpine AS frontend-build
WORKDIR /frontend
COPY frontend/package.json ./
RUN npm install --no-audit --no-fund
COPY frontend/ ./
RUN npm run build

# Stage 2: install Python dependencies away from the runtime stage.
FROM python:3.12-alpine AS python-deps
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 PIP_NO_CACHE_DIR=1
WORKDIR /build
RUN apk add --no-cache build-base libffi-dev
COPY requirements.txt ./
RUN pip install --prefix=/install -r requirements.txt

# Stage 3: lean, unprivileged runtime.
FROM python:3.12-alpine AS runtime
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PORT=8000
RUN addgroup -S app && adduser -S -G app -u 10001 app
WORKDIR /app
COPY --from=python-deps /install /usr/local
COPY --chown=app:app app/ ./app/
COPY --from=frontend-build --chown=app:app /frontend/dist ./app/static/
USER 10001:10001
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=2)" || exit 1
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
