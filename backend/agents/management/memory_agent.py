from services.memory_service import memory_service


async def memory_agent_node(state):

    print("\n🧠 Memory Agent")

    project_id = await memory_service.create_project(
        state["idea"]
    )

    state["project_id"] = project_id

    await memory_service.log(
        project_id,
        "Memory Agent",
        "Project initialized."
    )

    print(f"✅ Project Created : {project_id}")

    return state