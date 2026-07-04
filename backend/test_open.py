# test_openrouter.py

from llm import safe_invoke

prompt = """
You are a helpful AI.

Tell me:
1. What is Python?
2. Why is it popular?
"""

response = safe_invoke(prompt)

print(response.content)