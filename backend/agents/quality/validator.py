import json

def validator_node(state):

    try:
        data = json.loads(state["code"])
    except Exception:
        return {
            "valid": False,
            "reason": "Developer returned invalid or truncated JSON."
        }

    files = data.get("files", [])

    if len(files) < 5:
        return {
            "valid": False,
            "reason": "Too few files generated."
        }

    return {
        "valid": True,
        "reason": "PASS"
    }