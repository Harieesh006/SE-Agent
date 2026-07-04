# quota_test.py

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

for model in [
    "gemini-2.5-flash",
    "gemini-2.5-flash-lite",
    "gemini-2.0-flash"
]:
    try:
        response = client.models.generate_content(
            model=model,
            contents="hello"
        )
        print(model, "WORKS")
        print(response.text)

    except Exception as e:
        print(model, "FAILED")
        print(e)