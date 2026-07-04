from agents.product_manager import product_manager
from agents.architect import architect
from agents.planner import planner

prd = product_manager(
    "Build a food delivery app for college students"
)

architecture = architect(prd)

plan = planner(architecture)

print(plan)