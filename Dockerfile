FROM ollama/ollama:latest

# Expose Ollama's default port
EXPOSE 11434

# Start Ollama server and pull the model at runtime
CMD ["bash", "-c", "ollama serve & sleep 5 && ollama pull phi3:mini && tail -f /dev/null"]
