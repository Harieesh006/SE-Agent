from llm import safe_invoke

def devops_developer_node(state):

    prompt = f"""
You are a Senior DevOps Engineer.

PRD:
{state['prd']}

ARCHITECTURE:
{state['architecture']}

Generate ONLY DevOps files.

Generate:

- Dockerfile
- docker-compose.yml
- .env.example
- .gitignore

Rules:

- DevOps only
- Valid JSON only

Return:

{{
  "files":[
    {{
      "path":"Dockerfile",
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

            "path":"Dockerfile",

            "content":response.content

        }

    ]

}