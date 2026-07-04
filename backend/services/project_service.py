class ProjectService:
    def __init__(self):
        self.projects = {}

    def create_project(self, idea: str) -> str:
        import uuid
        pid = str(uuid.uuid4())[:8]
        self.projects[pid] = {"idea": idea, "status": "created"}
        return pid

    def get_project(self, project_id: str):
        return self.projects.get(project_id)

    def update_project(self, project_id: str, data: dict):
        if project_id in self.projects:
            self.projects[project_id].update(data)


project_service = ProjectService()
