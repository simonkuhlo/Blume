from typing import Optional

from fastapi import HTTPException
from sqlalchemy import select
from database import session
from models import User
from schemas.user import UserRead, UserCreate, UserUpdate

def read_user(user_id: int) -> Optional[UserRead]:
    db_item = session.query(User).filter(User.id == user_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="User not found")
    return UserRead.model_validate(db_item)

def create_user(user: UserCreate) -> UserRead:
    db_item = User(**user.model_dump())
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return UserRead.model_validate(db_item)

def update_user(user: UserUpdate, user_id: int) -> UserRead:
    db_item = session.query(User).filter(User.id == user_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="User not found")
    update_data = user.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_item, key, value)
    session.commit()
    session.refresh(db_item)
    return UserRead.model_validate(db_item)

def delete_user(user_id: int) -> None:
    session.query(User).filter(User.id == user_id).delete()
    session.commit()
