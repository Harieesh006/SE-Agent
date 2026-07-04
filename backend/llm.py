import os
import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    default_headers={
        "HTTP-Referer": "https://se-agent.local",
        "X-Title": "SE-Agent",
    },
    timeout=180,
)

MODEL = "google/gemma-4-31b-it:free"


class LLMResponse:
    def __init__(self, content):
        self.content = content


def safe_invoke(prompt, model=MODEL, max_tokens=8192):
    for attempt in range(3):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
            )
            if isinstance(response, str):
                return LLMResponse(response)
            return LLMResponse(response.choices[0].message.content)
        except Exception as e:
            err_str = str(e)
            print(f"[LLM Retry {attempt + 1}] {err_str[:120]}")
            if "429" in err_str or "rate" in err_str.lower():
                time.sleep(2 ** attempt)
                continue
    return LLMResponse("")


class _LLM:
    def invoke(self, prompt):
        return safe_invoke(prompt)


llm = _LLM()
