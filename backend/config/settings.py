import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
MONGODB_URI = os.getenv("MONGODB_URI", "")
DATABASE_NAME = os.getenv("DATABASE_NAME", "se_agent")
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "generated_project")
MAX_FILES = int(os.getenv("MAX_FILES", "15"))
SWARM_WORKERS = int(os.getenv("SWARM_WORKERS", "6"))
MAX_ITERATIONS = int(os.getenv("MAX_ITERATIONS", "10"))
