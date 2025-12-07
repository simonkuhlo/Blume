import os
from typing import Annotated

from fastapi import APIRouter, HTTPException, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from crud import entry as entry_crud
from schemas.entry import EntryCreate

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

# Configure Jinja2 templates directory
templates = Jinja2Templates(directory=f"{BASE_DIR}/templates")
router = APIRouter(prefix="/tests")

@router.post("/entry/create")
async def create_otp(request: Request, new_entry: Annotated[EntryCreate, Form()]):
    new_entry = EntryCreate()
    created_entry = entry_crud.create(new_entry)
    return created_entry