# merge_agent.py

import json


def merge_agent_node(state):

    print("\nRunning Merge Agent...")

    merged = {
        "files": []
    }

    outputs = state.get("developer_outputs", [])

    for output in outputs:

        if not output:
            continue

        try:

            if isinstance(output, str):

                data = json.loads(output)

            elif isinstance(output, dict):

                data = output

            else:

                continue

            if "files" in data:

                merged["files"].extend(data["files"])

        except Exception as e:

            print(f"⚠ Merge Error : {e}")

    unique = {}

    for file in merged["files"]:

        unique[file["path"]] = file

    merged["files"] = list(unique.values())

    state["merged_project"] = merged

    print(f"✅ {len(merged['files'])} Files Merged")

    return state