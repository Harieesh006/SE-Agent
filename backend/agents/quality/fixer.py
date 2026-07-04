from llm import safe_invoke

def fixer_node(state):

    prompt = f"""
You are a Senior Software Engineer.

PROJECT:
{state['code']}

REVIEW:
{state['review']}

Apply all fixes.

Rules:

1. Fix bugs.
2. Add missing features.
3. Improve architecture.
4. Improve security.
5. Improve scalability.

Return updated JSON project only.

No markdown.
Only JSON.
"""

    response = safe_invoke(prompt)

    return {
        "code": response.content
    }