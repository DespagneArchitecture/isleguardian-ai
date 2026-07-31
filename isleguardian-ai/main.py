from fastapi import FastAPI
import uvicorn
import ollama

app = FastAPI()

@app.post("/api/generate")
async def generate(payload: dict):
    prompt = payload.get("prompt", "")
    model = payload.get("model", "phi3:mini")

    response = ollama.generate(model=model, prompt=prompt)
    return {"response": response["response"]}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
