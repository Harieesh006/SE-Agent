import datetime


class LoggingService:
    def log(self, agent: str, message: str, project_id: str = ""):
        ts = datetime.datetime.now().isoformat()
        prefix = f"[{ts}]"
        if project_id:
            prefix += f" [{project_id}]"
        print(f"{prefix} [{agent}] {message}")

    def error(self, agent: str, message: str):
        self.log(agent, f"ERROR: {message}")


logging_service = LoggingService()
