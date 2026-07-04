from llm import safe_invoke

def devops_node(state):

    prompt = f"""
    You are a Senior DevOps Engineer.

    Project Requirements:
    {state.get('prd', '')}

    Architecture:
    {state.get('architecture', '')}

    Plan:
    {state.get('plan', '')}

    Generate:

    1. Dockerfile
    2. docker-compose.yml
    3. Kubernetes Deployment YAML
    4. Kubernetes Service YAML
    5. GitHub Actions CI/CD Pipeline
    6. AWS Deployment Strategy
    7. Monitoring Setup
    8. Logging Setup
    9. Security Checklist

    Return structured output only.
    """

    response = safe_invoke(prompt)

    return {
        "devops_report": response.content
    }