from llm import safe_invoke

def database_developer_node(state):

    prompt = f"""
You are a Senior Database Architect.

PROJECT REQUIREMENTS

{state["prd"]}

ARCHITECTURE

{state["architecture"]}

TASK

{state["current_task"]}

CODING STANDARDS

{state["patterns"]}

Generate ONLY database files.

Tech Stack:

- PostgreSQL
- SQLAlchemy
- Alembic

Generate:

- backend/database.py
- backend/models.py
- backend/alembic.ini
- backend/migrations/init.py

Rules:

- Database files only
- Valid JSON only

Return:

{{
  "files":[
    {{
      "path":"backend/models.py",
      "content":"..."
    }}
  ]
}}

Return ONLY JSON.
"""

    response = safe_invoke(prompt)

    return {

    "files":[

        {

            "path":"backend/models.py",

            "content":response.content

        }

    ]

}