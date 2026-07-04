from llm import safe_invoke


def devops_engineer_node(state):
    prompt = f"""
You are a Senior DevOps Engineer.

PRD:
{state.get('prd', '')}

Architecture:
{state.get('architecture', '')}

Generate Docker, CI/CD, and deployment configs.
Return ONLY JSON with files array.
"""

    response = safe_invoke(prompt)
    return {"files": [{"path": "Dockerfile", "content": response.content}]}
