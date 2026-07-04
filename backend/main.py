import sys
import json
from graph import graph


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <project idea>")
        print("   or: python main.py --file <path/to/ideas.json>")
        sys.exit(1)

    if sys.argv[1] == "--file":
        filepath = sys.argv[2]
        with open(filepath, "r") as f:
            ideas = json.load(f)
        if isinstance(ideas, list):
            for idea in ideas:
                run_single(idea if isinstance(idea, str) else idea.get("idea", ""))
        else:
            run_single(ideas.get("idea", ""))
    else:
        idea = " ".join(sys.argv[1:])
        run_single(idea)


def run_single(idea: str):
    if not idea:
        print("Error: Empty idea")
        return

    result = graph.invoke({"idea": idea})

    print("\n========== RESULT SUMMARY ==========")
    print(f"Status: {result.get('status')}")
    print(f"PRD: {len(result.get('prd', ''))} chars")
    print(f"Architecture: {len(result.get('architecture', ''))} chars")
    print(f"Plan: {len(result.get('plan', ''))} chars")
    print(f"Code: {len(result.get('code', ''))} chars")
    print(f"Review: {len(result.get('review', ''))} chars")
    print(f"Files Created: {result.get('files_created')}")
    print(f"Quality Score: {result.get('quality_score')}")
    print(f"Security Score: {result.get('security_score')}")
    print("===================================\n")


if __name__ == "__main__":
    main()
