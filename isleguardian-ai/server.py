from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from groq import Groq
import os

app = FastAPI()

# Load Groq API key from Render environment variables
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class GenerateRequest(BaseModel):
    model: str
    prompt: str

@app.post("/api/generate")
async def generate(req: GenerateRequest):
    try:
        completion = client.chat.completions.create(
            model=req.model,
            messages=[
                {"role": "user", "content": req.prompt}
            ]
        )
        return {"response": completion.choices[0].message.content}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Required for Render to start Uvicorn properly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "server:app",
        host="0.0.0.0",
        port=10000,
        reload=False
    )
