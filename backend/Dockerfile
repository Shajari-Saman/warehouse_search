FROM python:3.12-slim

# install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app

# copy file for dependency
COPY pyproject.toml uv.lock* ./

# install dependency 
RUN uv sync --frozen --no-dev

# copy source of program
COPY app ./app

EXPOSE 8000

CMD ["uv","run","uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
