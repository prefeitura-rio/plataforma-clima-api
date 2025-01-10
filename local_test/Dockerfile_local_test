FROM python:3.12-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy the app
ADD . /app
WORKDIR /app

# Install apt dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends libexpat1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

    # RUN apt-get update -qq || { echo "apt-get update failed"; exit 1; }
    # RUN apt-get install -y --no-install-recommends curl libexpat1 || { echo "apt-get install failed"; exit 1; }
    # RUN apt-get clean && rm -rf /var/lib/apt/lists/*

    # Install dependencies
RUN uv sync

# Run the app
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--loop", "asyncio", "--proxy-headers", "--forwarded-allow-ips=*"]