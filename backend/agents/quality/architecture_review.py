from llm import safe_invoke

def architecture_review_node(state):

    prompt = f"""
You are a Staff Software Architect.

ARCHITECTURE:
{state['architecture']}

PROJECT FILES:
{state.get('generated_files', [])}

Review:

1. Scalability
2. Maintainability
3. Modularity
4. Security
5. Performance

Return structured review.
"""

    response = safe_invoke(prompt)

    return {
        "architecture_review": response.content
    }
