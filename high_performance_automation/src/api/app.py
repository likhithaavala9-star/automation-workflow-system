from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.services.workflow_engine import WorkflowEngine
from src.services.task_manager import TaskManager
from src.database.db import engine, Base

# Create DB tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI()

# Initialize services
task_manager = TaskManager()
workflow_engine = WorkflowEngine()

# ENABLE CORS (IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# HOME ROUTE
@app.get("/")
def home():
    return {
        "message": "High Performance Automation System Running"
    }

# RUN WORKFLOW
@app.get("/run-workflow")
async def run_workflow():

    db_tasks = task_manager.get_pending_tasks()

    if not db_tasks:
        return {
            "workflow_status": "no pending tasks found",
            "results": [],
            "total_execution_time": 0
        }

    task_names = [task.task_name for task in db_tasks]

    output = await workflow_engine.execute_workflow(task_names)

    # Handle success / failure safely
    if isinstance(output, tuple):
        results, total_time = output
    else:
        return output  # error case

    return {
        "workflow_status": "completed",
        "results": results,
        "total_execution_time": total_time
    }

# GET TASKS
@app.get("/tasks")
def get_tasks():
    tasks = task_manager.get_all_tasks()
    return tasks

# CREATE TASK
@app.post("/create-task")
def create_task(task_name: str, task_type: str):

    task = task_manager.create_task(task_name, task_type)

    return {
        "task_id": task.task_id,
        "task_name": task.task_name,
        "status": task.status
    }

# METRICS
@app.get("/metrics")
def get_metrics():
    return workflow_engine.monitor.get_metrics()