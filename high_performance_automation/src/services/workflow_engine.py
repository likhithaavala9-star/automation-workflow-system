import asyncio
import time

from src.utils.logger import get_logger
logger = get_logger("workflow_engine")

from src.services.monitoring_service import MonitoringService
from src.services.task_strategies import (
    DownloadDataStrategy,
    ProcessDataStrategy,
    GenerateReportStrategy
)
from src.services.task_manager import TaskManager


class WorkflowEngine:
    def __init__(self):
        self.cache = {}
        self.task_manager = TaskManager()
        self.monitor = MonitoringService()

    def get_strategy(self, task_name):
        strategies = {
            "download_data": DownloadDataStrategy(),
            "process_data": ProcessDataStrategy(),
            "generate_report": GenerateReportStrategy()
        }
        return strategies.get(task_name)

    async def execute_task(self, task_name):
        try:
            logger.info(f"Starting task: {task_name}")

            # ✅ CACHE CHECK
            if task_name in self.cache:
                logger.info(f"Fetching from cache: {task_name}")

                self.monitor.record_task("completed", 0)

                return {
                    "task": task_name,
                    "status": "completed",
                    "execution_time": 0,
                    "cached": True
                }

            start_time = time.time()

            strategy = self.get_strategy(task_name)

            # ❌ NO STRATEGY FOUND
            if not strategy:
                logger.error(f"No strategy found for task: {task_name}")

                self.task_manager.update_task_status(task_name, "failed")

                self.monitor.record_task("failed", 0)

                return {
                    "task": task_name,
                    "status": "failed",
                    "message": "No strategy found"
                }

            # 🚀 EXECUTE TASK
            result = await strategy.execute()

            execution_time = round(time.time() - start_time, 2)

            result["execution_time"] = execution_time
            result["cached"] = False

            logger.info(f"Completed task: {task_name}")

            # ✅ UPDATE DATABASE
            self.task_manager.update_task_status(task_name, "completed")

            # ✅ RECORD METRICS
            self.monitor.record_task(
                result["status"],
                execution_time
            )

            # ✅ CACHE RESULT
            self.cache[task_name] = result

            return result

        except Exception as e:
            logger.error(f"Error in task {task_name}: {str(e)}")

            self.task_manager.update_task_status(task_name, "error")

            self.monitor.record_task("failed", 0)

            return {
                "task": task_name,
                "status": "error",
                "message": str(e)
            }

    async def execute_workflow(self, tasks):
        start_time = time.time()

        try:
            task_objects = [self.execute_task(task) for task in tasks]
            results = await asyncio.gather(*task_objects)

            total_time = round(time.time() - start_time, 2)

            return results, total_time

        except Exception as e:
            return {
                "workflow_status": "failed",
                "error": str(e)
            }