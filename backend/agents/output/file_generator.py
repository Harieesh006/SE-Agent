from llm import safe_invoke

def file_generator_node(state, file_info):

    path = file_info["path"]
    description = file_info["description"]

    prompt = f"""
You are a Senior Software Engineer.

PROJECT REQUIREMENTS:
{state['prd']}

ARCHITECTURE:
{state['architecture']}

Generate ONLY ONE FILE.

File Path:
{path}

Description:
{description}

Rules:

1. Return ONLY code.
2. No markdown.
3. No explanations.
4. Production-ready code.
5. Include imports.
6. Keep consistent with FastAPI/React architecture.

Generate the file content now.
"""

    response = safe_invoke(prompt)

    return {
        "path": path,
        "content": response.content
    }