from fastapi.requests import Request
from fastapi import status
from fastapi.exceptions import HTTPException
from .crud_handler_router import CRUDHandlerRouter
from crud import question_collection as question_collection_crud, question as question_crud
from schemas.question import QuestionCreate, QuestionUpdate

router = CRUDHandlerRouter(question_collection_crud)

@router.put("/{question_collection_id}/add_question/{question_id}")
async def create_otp(request: Request,question_collection_id: int, question_id: int):
    question_collection = question_collection_crud.get(question_collection_id)
    if not question_collection:
        raise HTTPException(status_code=404, detail="Question collection not found")
    question = question_crud.get(question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    question_collection.questions.append(question)
    return question_collection_crud.update(question_collection.id, QuestionUpdate.model_validate(question_collection))