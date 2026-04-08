from src.services.task_strategies import (
    DownloadDataStrategy,
    ProcessDataStrategy,
    GenerateReportStrategy
)

class StrategyFactory:

    @staticmethod
    def get_strategy(task_name):
        if task_name == "download_data":
            return DownloadDataStrategy()
        elif task_name == "process_data":
            return ProcessDataStrategy()
        elif task_name == "generate_report":
            return GenerateReportStrategy()
        else:
            return None