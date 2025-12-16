from typing import Optional
from pydantic import BaseModel
from schemas.question import QuestionRef


class Update(BaseModel):
    title: Optional[str]
    description: Optional[str]
    question_ids: Optional[list[int]] = None

    class Config:
        from_attributes = True