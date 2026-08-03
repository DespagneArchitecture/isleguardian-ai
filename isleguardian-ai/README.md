# IsleGuardian AI Worker  
A lightweight, self‑hosted AI service for the IsleGuardian Discord bot, powered by **Ollama** and the **Phi‑3 Mini** model.  
This worker runs on a Render Background Worker using a Dockerfile that installs and serves the model 24/7.

---

## 🚀 Overview
This service provides **free, unlimited AI responses** for the IsleGuardian bot without relying on OpenAI or paid API usage.  
It exposes a simple HTTP endpoint that the bot can call to generate text using the Phi‑3 Mini model.

---

## 🧠 Model
**Model:** `phi3:mini`  
**Provider:** Ollama  
**Features:**
- Fast and lightweight  
- Great for command explanations, FAQs, and help responses  
- Runs fully on your Render instance  
- No external API keys required  

---

## 🏗️ Deployment (Render)
This repository is deployed as a **Render Background Worker** using Docker.

### Worker Requirements
- Environment: **Docker**
- Instance Type: **Starter** (or higher)
- Always On: **Yes**

### Deployment Steps
1. Create a new Background Worker on Render.  
2. Connect this repository.  
3. Select **Docker** as the environment.  
4. Deploy — Render will automatically:
   - Install Ollama  
   - Pull the Phi‑3 Mini model  
   - Start the AI server  

---

## 📡 API Endpoint
Once deployed, the worker exposes the Ollama API:
