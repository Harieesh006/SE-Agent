import json
import os

# Load memory
with open("memory/project_memory.json", "r") as f:
    memory = json.load(f)

# Get the latest project (last entry)
if memory["projects"]:
    latest = memory["projects"][-1]
    print(f"Extracting project: {latest['idea'][:50]}...")
    
    # Create the generated_project directory
    os.makedirs("generated_project", exist_ok=True)
    
    # Save the PRD, architecture, and review as documentation
    with open("generated_project/PRD.md", "w") as f:
        f.write(latest.get("prd", ""))
    
    with open("generated_project/ARCHITECTURE.md", "w") as f:
        f.write(latest.get("architecture", ""))
    
    with open("generated_project/REVIEW.md", "w") as f:
        f.write(latest.get("review", ""))
    
    print("✅ Project documentation saved!")
    print(f"  - generated_project/PRD.md")
    print(f"  - generated_project/ARCHITECTURE.md")
    print(f"  - generated_project/REVIEW.md")
else:
    print("No projects in memory!")
