from fastapi import FastAPI
from app.config.db import db
app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI Service Running"}