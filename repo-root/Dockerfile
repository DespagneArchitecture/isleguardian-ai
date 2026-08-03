# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy your application folder
COPY isleguardian-ai/ /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (Render uses 10000 internally)
EXPOSE 10000

# Start your server
CMD ["python", "server.py"]
