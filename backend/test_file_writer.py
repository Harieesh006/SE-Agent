from agents.file_writer import file_writer_node

state = {
    "code": """
    {
      "files":[
        {
          "path":"backend/main.py",
          "content":"print('Hello World')"
        }
      ]
    }
    """
}

print(file_writer_node(state))