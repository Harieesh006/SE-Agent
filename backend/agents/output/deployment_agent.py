from llm import safe_invoke


def deployment_agent_node(state):
    prompt = f"""
You are a Deployment Engineer.

Architecture:
{state.get('architecture', '')}

Plan:
{state.get('plan', '')}

Generate deployment scripts and configurations.
Return ONLY JSON with files array.
"""

    response = safe_invoke(prompt)
    return {"files": [{"path": "deploy.sh", "content": response.content}]}
