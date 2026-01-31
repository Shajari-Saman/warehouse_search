FROM python:3.12-slim

# نصب uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app

# کپی فایل‌های dependency
COPY pyproject.toml uv.lock* ./

# نصب وابستگی‌ها
RUN uv sync --frozen --no-dev

# کپی سورس
COPY app ./app

EXPOSE 8000

CMD ["uv","run","uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
