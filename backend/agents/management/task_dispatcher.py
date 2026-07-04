# task_dispatcher.py

import json
from llm import safe_invoke


def task_dispatcher_node(state):
    print("\nRunning Task Dispatcher...")

    prompt = f"""
You are a Senior Engineering Manager at Google.

Your responsibility is to divide the project into tasks
for each engineering team.

PROJECT REQUIREMENTS

{state["prd"]}

ARCHITECTURE

{state["architecture"]}

IMPLEMENTATION PLAN

{state["plan"]}

Generate ONLY valid JSON.

Format:

{{
    "tasks":[
        {{
            "agent":"backend",
            "title":"Authentication",
            "description":"Develop JWT Authentication APIs"
        }},
        {{
            "agent":"database",
            "title":"Database Schema",
            "description":"Design PostgreSQL tables"
        }},
        {{
            "agent":"frontend",
            "title":"Login UI",
            "description":"Build Login and Register pages"
        }}
    ]
}}

Rules

Assign tasks only to these agents

backend
frontend
database
devops
security
ai
qa
documentation

Return ONLY JSON.
"""

    response = safe_invoke(prompt)

    try:
        tasks = json.loads(response.content)

    except Exception:

        print("❌ Task Dispatcher returned invalid JSON")

        tasks = {
            "tasks": []
        }

    state["tasks"] = tasks["tasks"]

    print(f"✅ {len(state['tasks'])} Tasks Created")

    return state