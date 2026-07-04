from llm import safe_invoke

def frontend_developer_node(state):

    prompt = f"""
You are a Senior Frontend Engineer.

PROJECT REQUIREMENTS

{state["prd"]}

ARCHITECTURE

{state["architecture"]}

TASK

{state["current_task"]}

CODING STANDARDS

{state["patterns"]}

Generate ONLY frontend files.

Tech Stack:

- React
- Axios
- React Router

Generate:

- frontend/package.json
- frontend/src/App.js
- frontend/src/api.js
- frontend/src/pages/Login.js
- frontend/src/pages/Register.js
- frontend/src/pages/Dashboard.js
- frontend/src/components/Navbar.js

Rules:

- Frontend only
- No backend
- No docker
- No README
- Valid JSON only

Return:

{{
  "files":[
    {{
      "path":"frontend/src/App.js",
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

            "path":"frontend/src/App.js",

            "content":response.content

        }

    ]

}