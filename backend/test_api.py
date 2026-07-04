from llm import llm

print("MODEL =", llm.model)

response = llm.invoke("Hello")

print(response.content)