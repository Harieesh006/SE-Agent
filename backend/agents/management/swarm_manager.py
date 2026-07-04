from concurrent.futures import ThreadPoolExecutor, as_completed

from agents.developers.backend_developer import backend_developer_node
from agents.developers.frontend_developer import frontend_developer_node
from agents.developers.database_developer import database_developer_node
from agents.developers.devops_developer import devops_developer_node
from agents.developers.security_agent import security_agent_node
from agents.quality.qa_engineer import qa_engineer_node


def swarm_manager_node(state):

    print("\nRunning Swarm Manager...")

    task_map = {
        "backend": backend_developer_node,
        "frontend": frontend_developer_node,
        "database": database_developer_node,
        "devops": devops_developer_node,
        "security": security_agent_node,
        "qa": qa_engineer_node,
    }

    developer_outputs = []

    futures = []

    with ThreadPoolExecutor(max_workers=6) as executor:

        for task in state.get("tasks", []):

            agent = task["agent"]

            if agent not in task_map:

                print(f"Unknown Agent : {agent}")

                continue

            developer_state = state.copy()

            developer_state["current_task"] = task

            futures.append(
                executor.submit(
                    task_map[agent],
                    developer_state
                )
            )

        for future in as_completed(futures):

            try:

                result = future.result()

                developer_outputs.append(result)

            except Exception as e:

                print(f"Developer Error : {e}")

    state["developer_outputs"] = developer_outputs

    print(f"{len(developer_outputs)} Developer Tasks Completed")

    return state
