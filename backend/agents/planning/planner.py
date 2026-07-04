from llm import safe_invoke

def planner_node(state):

    prompt = f"""
    You are a Senior Project Manager.

    Architecture:

    {state['architecture']}

    Generate:

    1. Timeline
    2. Sprint Plan
    3. Milestones

    Return structured output only.
    """

    response = safe_invoke(prompt)

    return {
        "plan": response.content
    }