from typing import Annotated

from fastapi import Form

from .crud_handler_router import CRUDHandlerRouter
from fastapi.requests import Request
from crud import question
from schemas.question import QuestionUpdate, QuestionCreate

router = CRUDHandlerRouter(question)

@router.put("/from_form/{question_id}")
async def create_otp(request: Request, question_id: int, new_question: Annotated[QuestionUpdate, Form()]):
    updated_question = question.update(question_id, new_question)
    return updated_question

@router.post("/from_form")
async def create_otp(request: Request, new_question: Annotated[QuestionCreate, Form()]):
    updated_question = question.create(new_question)
    return updated_question