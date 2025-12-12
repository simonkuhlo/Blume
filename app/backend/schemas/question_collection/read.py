from typing import Optional
from pydantic import BaseModel
from ..question import QuestionRead

class Read(BaseModel):
    id: int
    title: Optional[str]
    description: Optional[str]
    questions: Optional[list[QuestionRead]]

    class Config:
        from_attributes = True