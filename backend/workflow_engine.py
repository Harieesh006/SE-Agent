from agents.planning.project_manager_ai import project_manager_ai_node
from agents.developers.developer import developer_node
from agents.developers.security_agent import security_agent_node
from agents.quality.reviewer import reviewer_node
from agents.quality.fixer import fixer_node
from agents.quality.refactor_agent import refactor_agent_node
from agents.developers.test_generator import test_generator_node


def run_dynamic_workflow(state):

    max_iterations = 10

    for _ in range(max_iterations):

        decision = project_manager_ai_node(state)

        next_agent = decision["next_agent"]

        print(f"\nPM Selected: {next_agent}")

        if next_agent == "developer":
            state.update(
                developer_node(state)
            )

        elif next_agent == "security":
            state.update(
                security_agent_node(state)
            )

        elif next_agent == "reviewer":
            state.update(
                reviewer_node(state)
            )

        elif next_agent == "fixer":
            state.update(
                fixer_node(state)
            )

        elif next_agent == "refactor":
            state.update(
                refactor_agent_node(state)
            )

        elif next_agent == "test_generator":
            state.update(
                test_generator_node(state)
            )

        elif next_agent == "finish":
            break

    return state
