from llm import safe_invoke
import json

def manifest_node(state):

    prompt = f"""
You are a Senior Software Architect.

PROJECT REQUIREMENTS:
{state['prd']}

ARCHITECTURE:
{state['architecture']}

PLAN:
{state['plan']}

Generate a complete project file manifest.

Rules:

1. Return ONLY valid JSON.
2. Do NOT generate code.
3. Generate file paths and descriptions only.
4. Include backend, frontend, docs, tests and deployment files.

Format:

{{
  "files": [
    {{
      "path": "backend/main.py",
      "description": "FastAPI application entry point"
    }},
    {{
      "path": "backend/auth.py",
      "description": "JWT authentication logic"
    }}
  ]
}}
"""

    response = safe_invoke(prompt)

    try:
        data = json.loads(response.content)
    except Exception:
        data = {
            "files": []
        }

    return {
        "manifest": data
    }