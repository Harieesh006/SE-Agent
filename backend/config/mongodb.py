# config/mongodb.py

import os

from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

env_path = BASE_DIR / ".env"

print("Loading:", env_path)

load_dotenv(env_path, override=True)

MONGODB_URI = os.getenv("MONGODB_URI")
print("Mongo URI:", MONGODB_URI)
DATABASE_NAME = os.getenv("DATABASE_NAME", "se_agent")

if not MONGODB_URI:
    raise ValueError("❌ MONGODB_URI not found in .env")



client = AsyncIOMotorClient(
    MONGODB_URI,
    maxPoolSize=50,
    minPoolSize=5,
    serverSelectionTimeoutMS=5000
)

db = client[DATABASE_NAME]


async def check_connection():
    try:
        await client.admin.command("ping")
        print("✅ MongoDB Atlas Connected")
        return True

    except Exception as e:
        print(f"❌ MongoDB Connection Failed : {e}")
        return False