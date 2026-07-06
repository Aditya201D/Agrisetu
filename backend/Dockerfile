FROM python:3.12-slim

WORKDIR /app

# Install system packages
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

# Copy backend source
COPY backend/ .

EXPOSE 8000

CMD uvicorn main:app --host 0.0.0.0 --port 8000
