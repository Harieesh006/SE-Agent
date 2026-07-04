from llm import safe_invoke

def backend_developer_node(state):
  prompt = f"""
You are a Principal Software Engineer at Google.

PROJECT REQUIREMENTS

{state["prd"]}

ARCHITECTURE

{state["architecture"]}

TASK

{state["current_task"]}

CODING STANDARDS

{state["patterns"]}

Your task is to generate a COMPLETE SOFTWARE PROJECT.

Requirements:

* Production ready
* Scalable
* Modular architecture
* Clean code
* Security best practices
* JWT authentication
* PostgreSQL
* Environment variables
* Docker support
* API documentation
* Error handling
* Logging
* Validation
* Database models
* CRUD operations

Backend:

* FastAPI
* SQLAlchemy
* Pydantic
* JWT Authentication
* PostgreSQL
* Alembic migrations
* Modular routers
* Services layer

Frontend:

* React
* Axios
* React Router
* Component based structure
* Dashboard pages
* Login/Register pages

Generate at least:

* README.md
* requirements.txt
* Dockerfile
* docker-compose.yml
* .env.example

Backend:

* main.py
* database.py
* auth.py
* config.py
* models.py
* schemas.py
* crud.py
* routers/*
* services/*
* utils/*

Frontend:

* package.json
* src/App.js
* src/api.js
* src/pages/*
* src/components/*
* src/services/*

IMPORTANT:

Return ONLY JSON.

No markdown.

No explanations.

No comments outside JSON.

Format:

{{
"files": [
{{
"path": "backend/main.py",
"content": "escaped code"
}}
]
}}

Rules:

* Escape all quotes.
* Escape newlines with \n.
* JSON must be valid for json.loads().
Generate an MVP project only.

Rules:

1. Maximum 15 files.
2. Keep file contents short.
3. Do not generate long README files.
4. Do not generate full frontend implementation.
5. Generate only skeleton code.
6. Response MUST be valid JSON.
*Maximum 15 files.
"""

  response = safe_invoke(prompt)

  return {

    "files":[

        {

            "path":"backend/auth.py",

            "content":response.content

        }

    ]

}
