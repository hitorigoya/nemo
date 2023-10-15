from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import List


engine = create_engine(
    "sqlite:///database.sqlite", connect_args={"check_same_thread": False}, echo=True
)


class Base(DeclarativeBase):
    pass


class UserTable(Base):
    __tablename__ = "user_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
    contents: Mapped[List["ContentTable"]] = relationship()


class ContentTable(Base):
    __tablename__ = "content_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))
    title: Mapped[str]
    content: Mapped[str]
