from app.database import Base
# from .models_main import board_user_association
# from .tasklist_model_base import TaskListModel

import sqlalchemy.dialects.postgresql as pg
from sqlalchemy import String
from sqlalchemy.orm import relationship, mapped_column, Mapped

import uuid


class BoardModelBase(Base):
    __tablename__ = 'boards'

    # uid = Column(pg.UUID, primary_key=True, unique=True, index=True, nullable=False)
    uid: Mapped[uuid.UUID] = mapped_column(pg.UUID(as_uuid=True),
                                            primary_key=True, unique=True, default=uuid.uuid4)

    # title = Column(String(50))
    title: Mapped[str] = mapped_column(String(50))

    # Relationships are implemented in models_main.py

    def __repr__(self):
        return f'Board:{self.title}; id:{self.uid}'
