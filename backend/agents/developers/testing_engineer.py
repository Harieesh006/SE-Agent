from llm import safe_invoke


def testing_engineer_node(state):
    files = state.get("generated_files", [])
    test_files = []

    for file in files:
        path = file.get("path", "")
        if not path.endswith(".py"):
            continue

        prompt = f"""
You are a QA Engineer.

Generate pytest tests for:
FILE: {path}
CODE: {file.get('content', '')}

Return ONLY code.
"""

        response = safe_invoke(prompt)
        test_path = path.replace(".py", "_test.py")
        test_files.append({"path": f"tests/{test_path}", "content": response.content})

    return {"test_files": test_files}
