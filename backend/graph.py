from schemas.state import AgentState

from agents.planning.product_manager import product_manager_node
from agents.planning.architect import architect_node
from agents.planning.planner import planner_node
from agents.planning.pattern_agent import pattern_agent_node

from agents.management.task_dispatcher import task_dispatcher_node
from agents.management.dependency_agent import dependency_agent_node
from agents.management.swarm_manager import swarm_manager_node
from agents.management.merge_agent import merge_agent_node
from agents.management.manifest import manifest_node

from agents.developers.developer import developer_node
from agents.developers.security_agent import security_agent_node
from agents.developers.security_score import security_score_node
from agents.developers.test_generator import test_generator_node

from agents.quality.reviewer import reviewer_node
from agents.quality.fixer import fixer_node
from agents.quality.validator import validator_node
from agents.quality.qa import qa_node
from agents.quality.architecture_review import architecture_review_node
from agents.quality.quality_score import quality_score_node
from agents.quality.refactor_agent import refactor_agent_node

from agents.output.file_writer import file_writer_node
from agents.output.project_generator import project_generator_node

from workflow_engine import run_dynamic_workflow


def run_pipeline(state):
    print("\n========== SE-Agent Pipeline ==========")
    print(f"Idea: {state.get('idea', '')[:80]}")
    print("=======================================\n")

    state["status"] = "running"

    # === PHASE 1: PLANNING ===
    print("\n--- Phase 1: Planning ---")
    state.update(product_manager_node(state))
    print("[OK] PRD generated")

    state.update(architect_node(state))
    print("[OK] Architecture designed")

    state.update(planner_node(state))
    print("[OK] Plan created")

    state = pattern_agent_node(state)
    print("[OK] Patterns defined")

    # === PHASE 2: TASK DISPATCH ===
    print("\n--- Phase 2: Task Dispatch ---")
    state = task_dispatcher_node(state)
    state = dependency_agent_node(state)

    # === PHASE 3: SWARM DEVELOPMENT (parallel) ===
    print("\n--- Phase 3: Swarm Development ---")
    state = swarm_manager_node(state)
    state = merge_agent_node(state)

    # === PHASE 4: QA & REVIEW ===
    print("\n--- Phase 4: Quality Assurance ---")
    state.update(qa_node(state))
    state.update(architecture_review_node(state))
    state.update(quality_score_node(state))

    # === PHASE 5: MAIN DEVELOPER ===
    print("\n--- Phase 5: Main Developer ---")
    state.update(developer_node(state))

    # === PHASE 6: VALIDATE ===
    state.update(validator_node(state))
    if state.get("valid"):
        print("[OK] Code validated")
    else:
        print(f"[WARN] Validation: {state.get('reason')}")

    # === PHASE 7: REVIEW & FIX LOOP ===
    print("\n--- Phase 6: Review & Fix ---")
    state.update(reviewer_node(state))
    state.update(fixer_node(state))
    state.update(security_agent_node(state))
    state.update(security_score_node(state))
    state.update(refactor_agent_node(state))
    state.update(test_generator_node(state))

    # === PHASE 8: FILE GENERATION ===
    print("\n--- Phase 7: File Generation ---")
    state.update(manifest_node(state))
    state.update(project_generator_node(state))

    # === PHASE 9: WRITE FILES ===
    state.update(file_writer_node(state))
    if state.get("files_created"):
        print("\n[SUCCESS] Project files written to disk!")
    else:
        print("\n[WARN] File writing had issues")

    state["status"] = "completed"
    print("\n========== Pipeline Complete ==========")
    return state


class Graph:
    def invoke(self, state_dict):
        state: AgentState = {
            "idea": state_dict.get("idea", ""),
            "prd": "",
            "architecture": "",
            "plan": "",
            "code": "",
            "review": "",
            "status": "pending",
        }
        state.update(state_dict)
        return run_pipeline(state)


graph = Graph()
