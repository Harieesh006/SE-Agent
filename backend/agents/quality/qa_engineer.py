from llm import llm

def qa_engineer_node(state):

    prompt = f"""
    You are a Senior QA Engineer.

    Requirements:
    {state['prd']}

    Architecture:
    {state['architecture']}

    Plan:
    {state['plan']}

    Generated Code:
    {state['development_tasks']}

    Generate:

    1. Missing Requirements
    2. Edge Cases
    3. Risks
    4. Test Cases
    5. Security Concerns

    Return structured output.
    """

    response = llm.invoke(prompt)

    return {

    "files":[

        {

            "path":"tests/test_api.py",

            "content":response.content

        }

    ]

}