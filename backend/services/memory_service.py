from datetime import datetime

from config.mongodb import db


class MemoryService:

    def __init__(self):
        self.projects = db["projects"]
        self.prds = db["prds"]
        self.architectures = db["architectures"]
        self.plans = db["plans"]
        self.tasks = db["tasks"]
        self.logs = db["logs"]
        self.components = db["reusable_components"]
        self.bugs = db["bug_history"]


    async def create_project(self, idea: str):

        project = {
            "idea": idea,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow(),
            "status": "running"
        }

        result = await self.projects.insert_one(project)

        return str(result.inserted_id)


    async def save_prd(self, project_id: str, prd: str):

        await self.prds.update_one(
            {"project_id": project_id},
            {
                "$set": {
                    "project_id": project_id,
                    "content": prd,
                    "updated_at": datetime.utcnow()
                }
            },
            upsert=True
        )


    async def get_prd(self, project_id: str):

        return await self.prds.find_one(
            {"project_id": project_id}
        )


    async def save_architecture(self, project_id: str, architecture: str):

        await self.architectures.update_one(
            {"project_id": project_id},
            {
                "$set": {
                    "project_id": project_id,
                    "content": architecture,
                    "updated_at": datetime.utcnow()
                }
            },
            upsert=True
        )


    async def get_architecture(self, project_id: str):

        return await self.architectures.find_one(
            {"project_id": project_id}
        )


    async def save_plan(self, project_id: str, plan: str):

        await self.plans.update_one(
            {"project_id": project_id},
            {
                "$set": {
                    "project_id": project_id,
                    "content": plan,
                    "updated_at": datetime.utcnow()
                }
            },
            upsert=True
        )


    async def get_plan(self, project_id: str):

        return await self.plans.find_one(
            {"project_id": project_id}
        )


    async def save_tasks(self, project_id: str, tasks):

        await self.tasks.update_one(
            {"project_id": project_id},
            {
                "$set": {
                    "project_id": project_id,
                    "tasks": tasks,
                    "updated_at": datetime.utcnow()
                }
            },
            upsert=True
        )


    async def get_tasks(self, project_id: str):

        return await self.tasks.find_one(
            {"project_id": project_id}
        )


    async def log(self, project_id: str, agent: str, message: str):

        await self.logs.insert_one({
            "project_id": project_id,
            "agent": agent,
            "message": message,
            "timestamp": datetime.utcnow()
        })


memory_service = MemoryService()