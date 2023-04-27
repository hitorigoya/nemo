from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import ForeignKey


engine = create_engine("sqlite:///database.sqlite", echo=True)
# db = Session(engine)


class Base(DeclarativeBase):
    pass


class UserTable(Base):
    __tablename__ = "user_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
    # contents: Mapped[list["ContentTable"]] = relationship(back_populates="user")


class ContentTable(Base):
    __tablename__ = "content_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))
    title: Mapped[str]
    content: Mapped[str]
    # user: Mapped["UserTable"] = relationship(back_populates="contents")
