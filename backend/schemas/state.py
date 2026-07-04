from typing import TypedDict


class AgentState(TypedDict):

    idea: str

    prd: str

    architecture: str

    plan: str

    code: str

    review: str

    status: str