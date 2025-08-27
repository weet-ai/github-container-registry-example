# Use Python 3.13 slim image as base
FROM python:3.13.6-slim

# Install UV
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

# Set working directory
WORKDIR /app

# Set debian frontend to non-interactive and use bash
ENV DEBIAN_FRONTEND=noninteractive
ENV SHELL=/bin/bash

# Copy UV configuration files
COPY pyproject.toml uv.lock* ./

RUN pip install -U pip uv && uv venv && uv sync --no-cache --frozen

# Copy application code
COPY . /app

# Set PYTHONPATH
ENV PYTHONPATH="/app/.venv/bin"

# Expose FastAPI default port
EXPOSE 8000

# Set the entrypoint to run FastAPI application
ENTRYPOINT ["uv", "run", "uvicorn", "src.myapp.main:app", "--host", "0.0.0.0", "--port", "8000"]