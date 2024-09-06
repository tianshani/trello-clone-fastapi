from app.database import Base
from .association_tables import board_user_association, user_task_association

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
import sqlalchemy.dialects.postgresql as pg

# from passlib.hash import bcrypt
from typing import List
import datetime as dt
import uuid


class UserModel(Base):
    __tablename__ = 'users'

    uid: Mapped[uuid.UUID] = mapped_column(pg.UUID(as_uuid=True),
                                            primary_key=True, unique=True, default=uuid.uuid4)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    signup_date: Mapped[str] = mapped_column(String, 
                                             default=dt.datetime.now().strftime('%a, %d/%m/%Y'))

    hashed_password: Mapped[str]

    # Relationships
    user_comments = relationship('CommentModel', back_populates='author')
    boards = relationship('BoardModel', secondary=board_user_association)
    tasks = relationship('TaskModel',secondary=user_task_association)

    def __repr__(self):
        return f'User:{self.username}; Email:{self.email}'
