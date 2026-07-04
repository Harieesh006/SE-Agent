from llm import safe_invoke

def security_agent_node(state):

    files = state.get("generated_files", [])

    findings = []

    for file in files:

        prompt = f"""
You are a Senior Application Security Engineer.

Review this file for security issues.

FILE:
{file['path']}

CODE:
{file['content']}

Check:

1. SQL Injection
2. JWT Issues
3. Hardcoded Secrets
4. Authentication Flaws
5. Authorization Flaws
6. Input Validation
7. Sensitive Data Exposure
8. Insecure Dependencies

Return:

PASS

or

FAIL

with findings.
"""

        response = safe_invoke(prompt)

        findings.append({
            "path": file["path"],
            "review": response.content
        })

    return {

    "files":[

        {

            "path":"backend/security.py",

            "content":response.content

        }

    ]

}