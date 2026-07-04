from agents.planning.product_manager import product_manager_node
from agents.planning.architect import architect_node
from agents.planning.planner import planner_node
from agents.developers.developer import developer_node
from agents.output.file_writer import file_writer_node

state = {
    "idea": "AI Powered Campus Placement Management System"
}

print("Running Product Manager...")
state.update(product_manager_node(state))

print("Running Architect...")
state.update(architect_node(state))

print("Running Planner...")
state.update(planner_node(state))

print("Running Developer...")
state.update(developer_node(state))

print("Running File Writer...")
state.update(file_writer_node(state))

print("\n===== FINAL STATUS =====")
print(state["status"])
