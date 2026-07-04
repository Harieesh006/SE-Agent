from llm import safe_invoke

def test_generator_node(state):

    generated_files = state.get("generated_files", [])

    test_files = []

    for file in generated_files:

        path = file["path"]

        if not path.endswith(".py"):
            continue

        prompt = f"""
You are a Senior QA Engineer.

Generate pytest test cases for:

FILE:
{path}

CODE:
{file['content']}

Rules:
1. Return ONLY code.
2. Use pytest.
3. Cover happy path.
4. Cover edge cases.
5. Cover error handling.
"""

        response = safe_invoke(prompt)

        test_path = path.replace(
            ".py",
            "_test.py"
        )

        test_files.append({
            "path": f"tests/{test_path}",
            "content": response.content
        })

    return {
        "test_files": test_files
    }