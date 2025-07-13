from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from app.agent import process_error
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
def analyze_error(
    error_message: str = Form(...),
    stack_trace: str = Form(...),
    language: str = Form(...)
):
    logging.info(f"Analysis requested | Lang: {language} | Error: {error_message[:60]}")
    return process_error(error_message, stack_trace, language)
