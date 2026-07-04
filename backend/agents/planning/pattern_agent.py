# pattern_agent.py

import json
from llm import safe_invoke


def pattern_agent_node(state):

    print("\nRunning Pattern Agent...")

    prompt = f"""
You are a Distinguished Software Engineer at Google.

Your responsibility is to define the coding standards
for the entire project.

PROJECT REQUIREMENTS

{state["prd"]}

ARCHITECTURE

{state["architecture"]}

Generate ONLY JSON.

Format

{{
    "patterns": {{

        "backend": {{
            "framework": "FastAPI",
            "architecture": "Layered Architecture",
            "style": "PEP8",
            "error_handling": "Central Exception Handler",
            "logging": "Structured Logging",
            "validation": "Pydantic"
        }},

        "frontend": {{
            "framework": "React",
            "style": "Functional Components",
            "routing": "React Router",
            "state": "Context API"
        }},

        "database": {{
            "orm": "SQLAlchemy",
            "naming": "snake_case",
            "migrations": "Alembic"
        }},

        "security": {{
            "authentication": "JWT",
            "password_hash": "bcrypt",
            "authorization": "RBAC"
        }}
    }}
}}

Return ONLY valid JSON.
"""

    response = safe_invoke(prompt)

    try:

        data = json.loads(response.content)

    except Exception:

        print("❌ Pattern JSON Error")

        data = {
            "patterns": {}
        }

    state["patterns"] = data["patterns"]

    print("✅ Coding Standards Generated")

    return state