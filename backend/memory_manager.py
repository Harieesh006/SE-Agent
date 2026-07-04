import json
import os

MEMORY_FILE = "memory/project_memory.json"


def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return {"projects": []}

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()

            if not content:
                return {"projects": []}

            return json.loads(content)

    except Exception as e:

        print("Memory load warning:", e)

        return {"projects": []}


def save_memory(memory):

    os.makedirs("memory", exist_ok=True)

    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(
            memory,
            f,
            indent=2,
            ensure_ascii=False
        )