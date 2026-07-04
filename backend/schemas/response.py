from typing import TypedDict, Any


class AgentResponse(TypedDict):
    success: bool
    data: Any
    error: str
