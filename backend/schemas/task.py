from typing import TypedDict, List


class Task(TypedDict):
    agent: str
    title: str
    description: str


class Dependency(TypedDict):
    agent: str
    depends_on: List[str]
    required_files: List[str]
    priority: int
