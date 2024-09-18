FROM python:3.12-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy the app
ADD . /app
WORKDIR /app

# Install dependencies
RUN uv sync

# Run the app
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--loop", "asyncio", "--proxy-headers", "--forwarded-allow-ips=*"]