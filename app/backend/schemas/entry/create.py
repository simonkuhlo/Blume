from pydantic import BaseModel


class EntryCreate(BaseModel):
    user_id: int
    published: bool = False