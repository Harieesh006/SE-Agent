from llm import llm

def qa_node(state):

    prompt = f"""
    You are a Senior QA Engineer.

    PROJECT REQUIREMENTS:
    {state['prd']}

    ARCHITECTURE:
    {state['architecture']}

    PROJECT PLAN:
    {state['plan']}

    Analyze the system and provide:

    1. Missing Requirements
    2. Edge Cases
    3. Risks
    4. Test Cases
    5. Security Concerns

    IMPORTANT:
    - Return structured output only
    - No greetings
    - No explanations
    """

    response = llm.invoke(prompt)

    return {
        "qa_report": response.content
    }