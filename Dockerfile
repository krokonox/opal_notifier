# Base image with Python and Poetry
FROM python:3.9-slim-buster

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Install AWS CLI
RUN curl "https://d1vvhvl2y92vvt.cloudfront.net/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install \
    && rm -rf awscliv2.zip ./aws

# Copy and install project dependencies using Poetry
COPY pyproject.toml poetry.lock /app/
RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev --no-root

# Copy the rest of the application code
COPY . /app

# Set the entry point command
CMD ["python", "main.py"]
