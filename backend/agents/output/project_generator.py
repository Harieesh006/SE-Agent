from agents.output.file_generator import file_generator_node


def project_generator_node(state):

    generated_files = []

    files = state["manifest"].get("files", [])

    for file_info in files:

        print(f"Generating {file_info['path']}")

        result = file_generator_node(
            state,
            file_info
        )

        generated_files.append(result)

    return {
        "generated_files": generated_files
    }
