#!/bin/bash

# Start FastAPI backend
uvicorn app.main:app --host 127.0.0.1 --port 8000 &

# Start Streamlit frontend
streamlit run ui/dashboard.py --server.port 8501
