class MonitoringService:
    def __init__(self):
        self.total_tasks = 0
        self.successful_tasks = 0
        self.failed_tasks = 0
        self.total_execution_time = 0

    def record_task(self, status, execution_time):
        self.total_tasks += 1
        self.total_execution_time += execution_time

        if status == "completed":
            self.successful_tasks += 1
        else:
            self.failed_tasks += 1

    def get_metrics(self):
        avg_time = 0
        if self.total_tasks > 0:
            avg_time = round(self.total_execution_time / self.total_tasks, 2)

        return {
            "total_tasks_executed": self.total_tasks,
            "successful_tasks": self.successful_tasks,
            "failed_tasks": self.failed_tasks,
            "average_execution_time": avg_time
        }
    