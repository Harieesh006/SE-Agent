from llm import safe_invoke

def reviewer_node(state):

    prompt = f"""
You are a Principal Software Engineer.

Review the generated software project.

PRD:
{state['prd']}

ARCHITECTURE:
{state['architecture']}

PLAN:
{state['plan']}

GENERATED CODE:
{state['code']}

Evaluate:

1. Requirement Coverage
2. Architecture Quality
3. Scalability
4. Security
5. Code Structure
6. Missing Features
7. Bugs
8. Improvements

Return:

REVIEW SCORE: X/10

STRENGTHS:
...

ISSUES:
...

FIXES REQUIRED:
...
"""

    response = safe_invoke(prompt)

    return {
        "review": response.content
    }