# Dockerfile for Twin Digital project
# Uses Python 3.11 and installs all required Python dependencies.
# The image is built from the repository root and expects a requirements.txt file.

FROM python:3.11-slim

# Install system dependencies needed for building some Python packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc g++ make git curl \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy only requirements first for caching
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . /app

# Expose typical ports (JupyterLab 8888, MLflow 5000)
EXPOSE 8888 5000

# Default command (overridden in docker‑compose)
CMD ["bash"]
