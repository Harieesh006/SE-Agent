# dependency_agent.py

import json
from llm import safe_invoke


def dependency_agent_node(state):

    print("\nRunning Dependency Agent...")

    tasks = state.get("tasks", [])

    prompt = f"""
You are a Senior Software Architect at Google.

Your job is to analyze software dependencies.

PROJECT REQUIREMENTS

{state["prd"]}

ARCHITECTURE

{state["architecture"]}

TASKS

{json.dumps(tasks, indent=2)}

For every task identify:

1. Dependencies
2. Required Files
3. Blocking Tasks
4. Execution Priority

Return ONLY JSON.

Format

{{
    "dependencies":[
        {{
            "agent":"backend",
            "depends_on":[
                "database"
            ],
            "required_files":[
                "models.py",
                "database.py"
            ],
            "priority":1
        }}
    ]
}}

Return ONLY valid JSON.
"""

    response = safe_invoke(prompt)

    try:

        dependency_data = json.loads(response.content)

    except Exception:

        print("❌ Dependency JSON Error")

        dependency_data = {
            "dependencies":[]
        }

    state["dependencies"] = dependency_data["dependencies"]

    print(f"✅ {len(state['dependencies'])} Dependencies Generated")

    return state