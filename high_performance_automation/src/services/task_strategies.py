import asyncio
from abc import ABC, abstractmethod


class TaskStrategy(ABC):
    @abstractmethod
    async def execute(self):
        pass


class DownloadDataStrategy(TaskStrategy):
    async def execute(self):
        await asyncio.sleep(1)
        return {
            "task": "download_data",
            "status": "completed"
        }


class ProcessDataStrategy(TaskStrategy):
    async def execute(self):
        await asyncio.sleep(1)
        return {
            "task": "process_data",
            "status": "completed"
        }


class GenerateReportStrategy(TaskStrategy):
    async def execute(self):
        await asyncio.sleep(1)
        return {
            "task": "generate_report",
            "status": "completed"
        }