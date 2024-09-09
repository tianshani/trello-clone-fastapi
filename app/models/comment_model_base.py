from ..database import Base

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
import sqlalchemy.dialects.postgresql as pg

import uuid
import datetime as dt


class CommentModelBase(Base):
    __tablename__ = 'comments'

    uid: Mapped[uuid.UUID] = mapped_column(pg.UUID(as_uuid=True),
                                           primary_key=True, unique=True, default=uuid.uuid4)

    content: Mapped[str]
    creation_date: Mapped[str] = mapped_column(
        default=str(dt.datetime.now().strftime('%a, %d/%m/%Y, %H:%M:%S'))
    )

    # Foreign Keys
    parent_task_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('tasks.uid'))
    author_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('users.uid'))

    # Relationships
    # parent_task = relationship('TaskModel', back_populates='comments')
    # author: Mapped[UserModel] = relationship('UserModel', back_populates='user_comments')