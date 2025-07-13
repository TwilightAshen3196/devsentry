#!/bin/bash

# Acitvate virtual python environment (change by your path for environemnt)
. .../venv/bin/activate

# install requirements to environment
pip3 install -r requirements

# Start FastAPI backend
uvicorn app.main:app --host 127.0.0.1 --port 8000 &

# Start Streamlit frontend
streamlit run ui/dashboard.py --server.port 8501
