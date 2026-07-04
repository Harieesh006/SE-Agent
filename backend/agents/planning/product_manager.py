from llm import safe_invoke

def product_manager_node(state):

    prompt = f"""
You are a Principal Product Manager at Google.

Project Idea:
{state['idea']}

Create a COMPLETE Product Requirements Document (PRD).

Include:

# Executive Summary
- Problem Statement
- Proposed Solution
- Business Value

# Target Users
- Primary Users
- Secondary Users

# User Personas

# User Stories
Format:
As a <user>
I want <goal>
So that <benefit>

Generate at least 20 user stories.

# Functional Requirements
Generate detailed requirements.

Include:
- Authentication
- Dashboard
- Profile Management
- Search
- Notifications
- Reports
- Admin Features
- AI Features

# Non Functional Requirements

Include:
- Scalability
- Security
- Performance
- Reliability
- Availability
- Accessibility

# Success Metrics

# Future Scope

Return markdown only.
"""

    response = safe_invoke(prompt)

    return {
        "prd": response.content
    }