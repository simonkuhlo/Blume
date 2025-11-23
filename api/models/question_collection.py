from typing import Optional
from sqlalchemy import String, Column
from .questions_in_collection import association_table
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from database import Base
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from question import Question

class QuestionCollection(Base):
    __tablename__ = "question_collection"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    questions: Mapped[list["Question"]] = relationship(secondary=association_table, back_populates="collections")

    def __repr__(self) -> str:
        return f"Question(id={self.id!r})"