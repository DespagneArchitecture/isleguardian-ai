FROM ubuntu:22.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    curl \
    bash \
    ca-certificates \
    zstd \
    python3 \
    python3-pip \
    && update-ca-certificates

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | bash

# Set working directory
WORKDIR /app

# Copy server code
COPY server.py server.py

# Install FastAPI + Uvicorn
RUN pip3 install fastapi uvicorn

# Expose API port
EXPOSE 8000

# Start Ollama, pull model, then start FastAPI server
CMD bash -c "ollama serve & sleep 5 && ollama pull phi3:mini && uvicorn server:app --host 0.0.0.0 --port 8000"
