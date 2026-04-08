from src.models.task_model import Task
from src.database.db import SessionLocal
from src.utils.logger import get_logger

logger = get_logger("task_manager")


class TaskManager:

    def create_task(self, task_name, task_type):
        db = SessionLocal()
        new_task = Task(
            task_name=task_name,
            task_type=task_type,
            status="pending"
        )
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        logger.info(f"Task created: {task_name}")
        db.close()
        return new_task

    def get_tasks(self):
        db = SessionLocal()
        tasks = db.query(Task).all()
        db.close()
        return tasks
    
    def get_tasks():
        tasks = task_manager.get_tasks()
        return tasks

    def get_pending_tasks(self):
        db = SessionLocal()
        tasks = db.query(Task).filter(Task.status == "pending").all()
        db.close()
        return tasks


    def update_task_status(self, task_name, status):
        db = SessionLocal()

        tasks = db.query(Task).filter(Task.task_name == task_name).all()

        if not tasks:
            print(f"No tasks found for: {task_name}")
            db.close()
            return []

        for task in tasks:
            task.status = status

        db.commit()

        print(f"Updated {len(tasks)} tasks → {status}")

        db.close()

        return True  