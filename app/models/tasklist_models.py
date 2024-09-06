from app.database import Base
# from . import board_models, task_models
# from .board_models import BoardModel
from .task_models import TaskModel

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
import sqlalchemy.dialects.postgresql as pg

import datetime as dt
import uuid


class TaskListModel(Base):
    __tablename__ = 'tasklists'

    uid: Mapped[uuid.UUID] = mapped_column(primary_key=True, unique=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String(50))

    # Foreign Keys
    parent_board_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('boards.uid'))

    # Relationships
    parent_board= relationship('BoardModel', back_populates='child_lists')
    child_tasks = relationship(list['TaskModel'], back_populates='parent_tasklist')

    def __repr__(self):
        return f'Tasklist:{self.title}; Id:{self.uid}, Parent board:{self.parent_board.title}'
