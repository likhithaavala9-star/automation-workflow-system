from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from src.database.db import Base


class Task(Base):

    __tablename__ = "tasks"

    task_id = Column(Integer, primary_key=True, index=True)
    task_name = Column(String, index=True)
    task_type = Column(String)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)