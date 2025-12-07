from data.database import session
from models import Entry
from schemas.entry import EntryRead, EntryCreate, EntryUpdate, EntryReadOwner
from .base import CRUDHandler

class EntryCRUD(CRUDHandler[Entry, EntryRead, EntryCreate, EntryUpdate]):

    def __init__(self):
        super().__init__("entry", session, Entry, EntryRead, EntryCreate, EntryUpdate)

    def create(self, data: EntryCreate) -> EntryReadOwner:
        db_item = Entry(**data.model_dump())
        self.session.add(db_item)
        self.session.commit()
        self.session.refresh(db_item)
        return EntryReadOwner.model_validate(db_item)

handler: EntryCRUD = EntryCRUD()