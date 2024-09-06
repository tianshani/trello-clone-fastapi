from sqlalchemy import Table, Column, ForeignKey
import sqlalchemy.dialects.postgresql as pg
from ..database import Base

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
