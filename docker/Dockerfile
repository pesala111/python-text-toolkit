FROM python:3.11-slim

WORKDIR /app

# Install uv
RUN pip install --no-cache-dir uv

# Copy only what we need (keeps image clean)
COPY pyproject.toml uv.lock README.md /app/
COPY src/ /app/src/

# Install the package (no dev deps)
RUN uv pip install --system -e .

# Default command: run the CLI
ENTRYPOINT ["textkit"]