import sys
sys.stdout.reconfigure(encoding='utf-8')  # type: ignore

from agents.planning.product_manager import product_manager_node
from agents.planning.architect import architect_node
from agents.planning.planner import planner_node
from agents.developers.developer import developer_node
from agents.output.file_writer import file_writer_node

state = {"idea": "Todo app with FastAPI and React"}

print("=== PM ===")
state.update(product_manager_node(state))
print(f"PRD: {len(state['prd'])} chars")

print("=== Architect ===")
state.update(architect_node(state))
print(f"Architecture: {len(state['architecture'])} chars")

print("=== Planner ===")
state.update(planner_node(state))
print(f"Plan: {len(state['plan'])} chars")

print("=== Developer ===")
state.update(developer_node(state))
print(f"Code: {len(state['code'])} chars")

print("=== File Writer ===")
state.update(file_writer_node(state))
print(f"Files created: {state.get('files_created')}")

print("\nPipeline test passed!")
