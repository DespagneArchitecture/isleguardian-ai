FROM ollama/ollama:latest

# Pull the model when the container starts
RUN ollama pull phi3:mini

# Expose Ollama's default port
EXPOSE 11434

# Start Ollama server
CMD ["ollama", "serve"]
