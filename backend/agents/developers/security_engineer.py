from llm import safe_invoke


def security_engineer_node(state):
    prompt = f"""
You are a Senior Security Engineer.

Architecture:
{state.get('architecture', '')}

Generate security configurations and auth code.
Return ONLY JSON with files array.
"""

    response = safe_invoke(prompt)
    return {"files": [{"path": "backend/security.py", "content": response.content}]}
