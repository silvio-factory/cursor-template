# backend/main.py

# Main entry point for the FastAPI application

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # If you need CORS
import uvicorn  # For running the server

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Add this if you want to run the server directly from this file
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
