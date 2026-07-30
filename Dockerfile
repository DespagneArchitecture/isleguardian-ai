FROM ubuntu:22.04

# Install dependencies
RUN apt-get update && apt-get install -y curl bash ca-certificates && update-ca-certificates

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | bash

# Expose Ollama port
EXPOSE 11434

# Start Ollama and pull model at runtime
CMD bash -c "
    ollama serve &
    sleep 5 &&
    ollama pull phi3:mini &&
    tail -f /dev/null
"
