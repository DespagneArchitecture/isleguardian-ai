FROM ollama/ollama:latest

# Install Python
RUN apt-get update && apt-get install -y python3 python3-pip

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Pull the model
RUN ollama pull phi3:mini

# Start Ollama server AND FastAPI
CMD ollama serve & python3 main.py
