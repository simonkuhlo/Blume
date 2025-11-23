from pydantic import BaseModel
from ..user import UserRead
from ..question import QuestionRead
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..entry import EntryRead

class EntryAnswerRead(BaseModel):
    id: int
    question: QuestionRead
    entry: "EntryRead"
    string_value: str
