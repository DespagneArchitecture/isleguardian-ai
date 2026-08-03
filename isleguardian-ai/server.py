from fastapi import FastAPI
from pydantic import BaseModel
import subprocess
import json

app = FastAPI()

class GenerateRequest(BaseModel):
    model: str
    prompt: str

@app.post("/api/generate")
def generate(req: GenerateRequest):
    # Call Ollama
    result = subprocess.run(
        ["ollama", "run", req.model],
        input=req.prompt.encode(),
        stdout=subprocess.PIPE
    )
    return {"response": result.stdout.decode()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "server:app",
        host="0.0.0.0",
        port=10000,
        reload=False
    )
