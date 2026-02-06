from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Text, String, Integer, DateTime, ForeignKey
from datetime import datetime


class Base(DeclarativeBase):
    pass


class Snippet(Base):
    __tablename__ = "snippets"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)


class SnippetVersion(Base):
    __tablename__ = "snippet_versions"

    id: Mapped[int] = mapped_column(primary_key=True)
    snippet_id: Mapped[int] = mapped_column(ForeignKey("snippets.id"))
    code: Mapped[str] = mapped_column(Text)
    version: Mapped[int]


class Execution(Base):
    __tablename__ = "executions"

    id: Mapped[int] = mapped_column(primary_key=True)
    snippet_version_id: Mapped[int] = mapped_column(ForeignKey("snippet_versions.id"))
    output: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(50))
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
