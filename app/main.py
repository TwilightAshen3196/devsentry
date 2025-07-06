from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.agent import process_error
import logging

app = FastAPI()

class ErrorReport(BaseModel):
    error_message: str
    stack_trace: str
    language: str = "python"

@app.post("/analyze")
async def analyze_error(payload: ErrorReport):
    try:
        result = await process_error(payload)
        return result
    except Exception as e:
        logging.error(f"Error in analysis: {e}")
        raise HTTPException(status_code=500, detail=str(e))