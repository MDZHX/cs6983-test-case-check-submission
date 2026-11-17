# The test-case environment: Python, the locked packages, the engine, and the cases.
# Build and run it with Docker Compose (compose.yaml); see README.md.
FROM python:3.12.11-slim

# uv, pinned, from its official image.
COPY --from=ghcr.io/astral-sh/uv:0.12.23 /uv /bin/uv

ENV PYTHONUNBUFFERED=1 \
    UV_PYTHON_DOWNLOADS=never \
    UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    TESTBED_IN_DOCKER=1

WORKDIR /app
# Install exactly what uv.lock lists (--locked fails if the lock is out of date with pyproject.toml).
COPY pyproject.toml uv.lock .python-version ./
RUN uv sync --locked --no-dev
ENV PATH="/app/.venv/bin:$PATH"

# The engine and the cases. compose.yaml also mounts cases/ and runs/ from your folder,
# so you can edit cases without rebuilding and the run folders land on your machine.
COPY run.py ./
COPY testbed/ testbed/
COPY cases/ cases/
COPY tests/ tests/

# Human mode serves its page on this port.
EXPOSE 8765
ENTRYPOINT ["python", "run.py"]
CMD ["--help"]
