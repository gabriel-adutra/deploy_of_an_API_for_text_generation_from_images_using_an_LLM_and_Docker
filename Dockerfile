# Define base image
ARG PYTHON_VERSION=3.11.5
FROM python:${PYTHON_VERSION}-slim AS base

# Install utility packages
RUN apt-get update && apt-get install -y procps && rm -rf /var/lib/apt/lists/*

# Install Rust compiler required for the LLM model
RUN curl https://sh.rustup.rs -sSf | bash -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# Prevent Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Prevent Python from buffering stdout and stderr to avoid situations where
# the application hangs without emitting any logs due to buffering
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Create log directory
RUN mkdir -p /var/log/vqa

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Download and install dependencies as a separate step to leverage Docker cache
RUN --mount=type=cache,target=/root/.cache/pip python -m pip install -r requirements.txt

# Copy source code to container
COPY . .

# Expose port where the application receives connections
EXPOSE 3000

# Run the API
CMD ["python", "backend/api/app.py"]
