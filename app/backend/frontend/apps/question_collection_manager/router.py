from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from frontend.jinja_templates import templates
from crud import question_collection as question_collection_crud

router = APIRouter(prefix="/question_collection_manager", tags=["question_collection_manager"])

@router.get("/", response_class=HTMLResponse)
async def main_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("apps/admin/question_collection_manager/question_collection_manager.j2", {"request": request})

@router.get("/browser", response_class=HTMLResponse)
async def admin_question_collection_browser(request: Request) -> HTMLResponse:
    question_collections = question_collection_crud.list()
    return templates.TemplateResponse("apps/admin/question_collection_manager/question_collection_browser.j2",
                                      {"request": request, "question_collections": question_collections})

@router.get("/editor/{collection_id}", response_class=HTMLResponse)
async def admin_question_editor(request: Request, collection_id: int) -> HTMLResponse:
    question_collection = question_collection_crud.get(collection_id)
    related_questions = None
    unrelated_questions = None
    return templates.TemplateResponse("apps/admin/question_collection_manager/question_collection_editor.j2",
                                      {"request": request,
                                       "question_collection": question_collection,
                                       "related_questions": related_questions,
                                       "unrelated_questions": unrelated_questions
                                       })