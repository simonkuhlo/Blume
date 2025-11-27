from pydantic import BaseModel
from ..question import QuestionRead

class EntryAnswerRead(BaseModel):
    id: int
    question: QuestionRead
    string_value: str
