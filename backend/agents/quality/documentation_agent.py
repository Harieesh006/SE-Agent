from llm import safe_invoke


def documentation_agent_node(state):
    prompt = f"""
You are a Technical Writer.

PRD:
{state.get('prd', '')}

Architecture:
{state.get('architecture', '')}

Code:
{state.get('code', '')[:2000]}

Generate project documentation: README, API docs, setup guide.
Return ONLY JSON with files array.
"""

    response = safe_invoke(prompt)
    return {"files": [{"path": "README.md", "content": response.content}]}
