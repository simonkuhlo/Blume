from typing import Optional

from pydantic import BaseModel

class Create(BaseModel):
    title: Optional[str] = "Untitled Collection"
    description: Optional[str] = None