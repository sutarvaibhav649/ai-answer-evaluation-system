from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

try:
    client = MongoClient(os.getenv("MONGO_URI"))
    db = client["answer_evaluation_ai"]
    print("MongoDB Connected in FastAPI")
except Exception as e:
    print("MongoDB FastAPI Error:", e)
