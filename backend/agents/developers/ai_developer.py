from llm import safe_invoke


def ai_developer_node(state):
    prompt = f"""
You are an AI/ML Engineer.

PRD:
{state.get('prd', '')}

Architecture:
{state.get('architecture', '')}

Generate AI/ML related code for the project.
Return ONLY JSON with files array.
"""

    response = safe_invoke(prompt)
    return {"files": [{"path": "backend/ai_service.py", "content": response.content}]}
