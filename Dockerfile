FROM ollama/ollama:latest

# Install Python
RUN apt-get update && apt-get install -y python3 python3-pip

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Pull the model at build time
RUN ollama pull phi3:mini

CMD ["python3", "main.py"]
