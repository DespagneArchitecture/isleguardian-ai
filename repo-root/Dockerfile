FROM ollama/ollama:latest

RUN apt-get update && apt-get install -y python3 python3-pip supervisor

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN ollama pull phi3:mini

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["supervisord", "-n"]
