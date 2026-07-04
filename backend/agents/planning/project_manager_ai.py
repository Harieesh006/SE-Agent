from llm import safe_invoke
import json

def project_manager_ai_node(state):

    prompt = f"""
You are an Engineering Manager.

Current Project State:

PRD:
{state.get('prd', '')[:1000]}

Architecture:
{state.get('architecture', '')[:1000]}

Review:
{state.get('review', '')[:1000]}

Security Score:
{state.get('security_score', 0)}

Quality Score:
{state.get('quality_score', 0)}

Available Agents:

- developer
- security
- reviewer
- fixer
- refactor
- test_generator
- finish

Decide the NEXT BEST ACTION.

Return JSON:

{{
    "next_agent": "developer"
}}
"""

    response = safe_invoke(prompt)

    try:
        return json.loads(response.content)
    except:
        return {
            "next_agent": "finish"
        }