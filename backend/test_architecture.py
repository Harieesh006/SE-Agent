from agents.product_manager import product_manager
from agents.architect import architect

prd = product_manager(
    "Build a food delivery app for college students"
)

architecture = architect(prd)

print(architecture)