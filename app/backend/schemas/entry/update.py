from typing import Optional
from pydantic import BaseModel


class EntryUpdate(BaseModel):
    published: Optional[bool]