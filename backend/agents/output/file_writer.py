import json
import os
import re



DEBUG_FOLDER = "debug"
OUTPUT_FOLDER = "generated_project"

def clean_json(raw_text):
    if not raw_text:
        return ""

    raw_text = raw_text.strip()

    # Remove markdown wrappers
    raw_text = re.sub(r"```json", "", raw_text)
    raw_text = re.sub(r"```", "", raw_text)

    # Find first JSON object
    start = raw_text.find("{")
    end = raw_text.rfind("}")

    if start != -1 and end != -1:
        raw_text = raw_text[start:end + 1]

    return raw_text.strip()


def save_debug_file(filename, content):
    os.makedirs(DEBUG_FOLDER, exist_ok=True)

    with open(
        os.path.join(DEBUG_FOLDER, filename),
        "w",
        encoding="utf-8"
    ) as f:
        f.write(content)


def parse_json(raw_output):
    cleaned = clean_json(raw_output)

    try:
        data = json.loads(cleaned)

        return True, data

    except json.JSONDecodeError as e:
        print("\n===== JSON PARSE ERROR =====")
        print("Message :", e.msg)
        print("Line    :", e.lineno)
        print("Column  :", e.colno)
        print("Position:", e.pos)

        save_debug_file(
            "broken_json.txt",
            cleaned
        )

        return False, None


def write_files(files):
    os.makedirs(
        OUTPUT_FOLDER,
        exist_ok=True
    )

    created = 0

    for file in files:
        try:
            path = file["path"]
            content = file["content"]

            full_path = os.path.join(
                OUTPUT_FOLDER,
                path
            )

            os.makedirs(
                os.path.dirname(full_path),
                exist_ok=True
            )

            with open(
                full_path,
                "w",
                encoding="utf-8"
            ) as f:
                f.write(content)

            print(f"Created: {full_path}")

            created += 1

        except Exception as ex:
            print(
                f"Failed to create file: {file}"
            )
            print(ex)

    return created


def write_project_files(raw_output):
    print("\nRunning File Writer...")

    save_debug_file(
        "developer_raw_output.txt",
        raw_output
    )

    print(
        "\n===== RAW OUTPUT PREVIEW ====="
    )

    print(raw_output[:1500])

    success, data = parse_json(raw_output)

    if not success:
        return False

    files = data.get("files", [])

    if not files:
        print(
            "\nNo files found in JSON."
        )

        return False

    created = write_files(files)

    print(
        f"\nTotal files created: {created}"
    )

    return created > 0

def file_writer_node(state):

        success = write_project_files(
        state["code"]
    )

        return {
        "files_created": success
    }
