from fastapi import FastAPI
import uvicorn
from src.myagent.agent import run
from pydantic import BaseModel


class TimeRequest(BaseModel):
    prompt: str


app = FastAPI()

@app.post("/get_time/")
async def get_time(req: TimeRequest):
    return await run(req.prompt)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)