from app.database import Base
from .association_tables import user_task_association

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
import sqlalchemy.dialects.postgresql as pg

import datetime as dt
import uuid


class TaskModel(Base):
    __tablename__ = 'tasks'
    
    uid: Mapped[uuid.UUID] = mapped_column(pg.UUID(as_uuid=True), primary_key=True, unique=True)
    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str]
    due_date: Mapped[ dt.datetime | None ]

    # Foreign Keys
    parent_tasklist_id: Mapped[uuid.UUID] = mapped_column(pg.UUID, ForeignKey('tasklists.uid'))

    # Relationships
    comments = relationship('CommentModel', back_populates='parent_task')
    users = relationship('UserModel', secondary=user_task_association)

    def __repr__(self):
        return f'Task:{self.title}; Description:{self.description[:10]}...'

