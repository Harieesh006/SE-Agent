from llm import safe_invoke

def architect_node(state):

    prompt = f"""
You are a Principal Software Architect at Google.

PRD:

{state['prd']}

Design a production-grade system.

Generate:

# High Level Architecture

# Component Diagram

# Frontend Architecture
- Framework
- Folder Structure
- State Management

# Backend Architecture
- Services
- Modules
- APIs

# Database Design
Generate tables with:
- Table Name
- Columns
- Relationships

# API Design
Generate:
- Endpoint
- Method
- Request
- Response

# Security Design
- JWT
- RBAC
- Encryption
- Rate Limiting

# Scalability Strategy
- Load Balancer
- Caching
- Queue System

# Cloud Deployment
- Docker
- Kubernetes
- CI/CD

# Monitoring
- Logging
- Metrics
- Alerts

Return detailed markdown.

Previous patterns:
{state.get('best_patterns', [])}
"""
    response = safe_invoke(prompt)

    return {
        "architecture": response.content
    }