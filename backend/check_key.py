from dotenv import load_dotenv
import os

load_dotenv()

print("Current Directory =", os.getcwd())
print("ENV FILE EXISTS =", os.path.exists(".env"))

print("GOOGLE_API_KEY =", os.getenv("GOOGLE_API_KEY"))