from typing import Optional
from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader
from fastapi import status

from crud import entry as entry_crud

security = APIKeyHeader(name="X-Article-Secret", auto_error=False)

async def verify_entry_secret(entry_id: int, secret: Optional[str] = Depends(security)):
    entry = entry_crud.get_admin(entry_id)
    if not entry or entry.secret != secret:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid article secret")
    return entry