from agents.planning.product_manager import product_manager_node
from agents.planning.architect import architect_node
from agents.planning.planner import planner_node
from agents.developers.developer import developer_node
from agents.output.file_writer import file_writer_node

state = {"idea": "Build a todo app with FastAPI and React"}
state.update(product_manager_node(state))
print(f"PRD: {len(state['prd'])} chars")

state.update(architect_node(state))
print(f"Architecture: {len(state['architecture'])} chars")

state.update(planner_node(state))
print(f"Plan: {len(state.get('plan', ''))} chars")

state.update(developer_node(state))
print(f"Code: {len(state.get('code', ''))} chars")

state.update(file_writer_node(state))
print(f"Files created: {state.get('files_created')}")

print("\nPipeline logic works!")
