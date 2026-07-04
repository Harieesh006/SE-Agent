from graph import graph

result = graph.invoke({
    "idea": "Build a food delivery app for college students"
})

print("\nPRD:\n")
print(result["prd"])

print("\nARCHITECTURE:\n")
print(result["architecture"])

print("\nQA REPORT:\n")
print(result["qa_report"])

print("\nPLAN:\n")
print(result["plan"])