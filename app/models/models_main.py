from sqlalchemy import Table, Column, ForeignKey
import sqlalchemy.dialects.postgresql as pg
from sqlalchemy.orm import relationship, Mapped

from ..database import Base
from . import (user_model_base, board_model_base, tasklist_model_base,
               task_model_base, comment_model_base)

import uuid


board_user_association = Table(
    'board_user_association', Base.metadata,
    Column('board_id', pg.UUID(as_uuid=True), ForeignKey('boards.uid'), primary_key=True ),
    Column('user_id', pg.UUID(as_uuid=True), ForeignKey('users.uid'), primary_key=True )
)

user_task_association = Table(
    'user_task_association', Base.metadata,
    Column('user_id', pg.UUID(as_uuid=True), ForeignKey('users.uid'), primary_key=True),
    Column('task_id', pg.UUID(as_uuid=True), ForeignKey('tasks.uid'), primary_key=True)
)


class UserModel(user_model_base.UserModelBase):
    user_comments: Mapped[ list['CommentModel'] ] = relationship(back_populates='author')
    boards: Mapped[ list['BoardModel'] ] = relationship(secondary=board_user_association)
    tasks: Mapped[ list['TaskModel'] ] = relationship(secondary=user_task_association)
    # TODO Check if M2M relationship needs class argument (after Mapped[])
    # TODO check if it needs list[Model] or just Model

class BoardModel(board_model_base.BoardModelBase):
    child_tasklists: Mapped[ list['TaskListModel'] ] = relationship(back_populates='parent_board')
    board_users: Mapped[ list['UserModel'] ] = relationship(secondary=board_user_association)

class TaskListModel(tasklist_model_base.TaskListModelBase):
    parent_board: Mapped['BoardModel'] = relationship(back_populates='child_tasklists')
    child_tasks: Mapped[ list['TaskModel'] ] = relationship(back_populates='parent_tasklist')

class TaskModel(task_model_base.TaskModelBase):
    parent_tasklist: Mapped['TaskListModel'] = relationship(back_populates='child_tasks')
    comments: Mapped[ list['CommentModel'] ] = relationship(back_populates='parent_task')
    users: Mapped['UserModel'] = relationship(secondary=user_task_association)

class CommentModel(comment_model_base.CommentModelBase):
    author: Mapped[ 'UserModel' ] = relationship(back_populates='user_comments')
    parent_task: Mapped['TaskModel'] = relationship(back_populates='comments')