FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    curl \
    bash \
    ca-certificates \
    zstd \
    python3 \
    python3-pip \
    && update-ca-certificates

RUN curl -fsSL https://ollama.com/install.sh | bash

WORKDIR /app
COPY server.py server.py

RUN pip3 install fastapi uvicorn

EXPOSE 8000

CMD bash -c "ollama serve & sleep 5 && ollama pull phi3:mini && uvicorn server:app --host 0.0.0.0 --port 8000"
