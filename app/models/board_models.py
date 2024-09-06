from app.database import Base
from .association_tables import board_user_association

import sqlalchemy.dialects.postgresql as pg
from sqlalchemy import String
from sqlalchemy.orm import relationship, mapped_column, Mapped

import uuid
import datetime as dt


class BoardModel(Base):
    __tablename__ = 'boards'

    # uid = Column(pg.UUID, primary_key=True, unique=True, index=True, nullable=False)
    uid: Mapped[uuid.UUID] = mapped_column(pg.UUID(as_uuid=True),
                                            primary_key=True, unique=True, default=uuid.uuid4)

    # title = Column(String(50))
    title: Mapped[str] = mapped_column(String(50))

    # Relationships
    child_lists = relationship(list['TaskListModel'], back_populates='parent_board')
    board_users = relationship('UserModel', secondary=board_user_association)

    def __repr__(self):
        return f'Board:{self.title}; id:{self.uid}'
