from llm import safe_invoke

def refactor_agent_node(state):

    files = state.get("generated_files", [])

    improved_files = []

    for file in files:

        prompt = f"""
You are a Principal Software Engineer.

Refactor this code.

FILE:
{file['path']}

CODE:
{file['content']}

Goals:

1. Improve readability
2. Improve naming
3. Remove duplication
4. Improve modularity
5. Improve error handling
6. Follow best practices
7. Keep functionality unchanged

Return ONLY code.
"""

        response = safe_invoke(prompt)

        improved_files.append({
            "path": file["path"],
            "content": response.content
        })

    return {
        "generated_files": improved_files
    }