from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from groq import Groq
import os

app = FastAPI()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class GenerateRequest(BaseModel):
    model: str
    prompt: str

VALID_GROQ_MODELS = {
    "llama3-groq-8b-8192",
    "llama3-groq-70b-8192",
    "gemma2-9b-it",
    "mixtral-8x7b-32768"
}

@app.post("/api/generate")
async def generate(req: GenerateRequest):
    if req.model not in VALID_GROQ_MODELS:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported model. Use one of: {', '.join(VALID_GROQ_MODELS)}"
        )

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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=10000)
