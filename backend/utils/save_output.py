import os


def save_output(filename, content):

    os.makedirs("outputs", exist_ok=True)

    with open(
        os.path.join("outputs", filename),
        "w",
        encoding="utf-8"
    ) as f:
        f.write(content)