from typing import Optional
from pydantic import BaseModel
from ..answer_type import AnswerType

class Create(BaseModel):
    title: str = "Unnamed Question"
    description: Optional[str] = ""
    short: Optional[bool] = False
    #answer_type: AnswerType