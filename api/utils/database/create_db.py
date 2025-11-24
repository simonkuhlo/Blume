from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import User
from models.base import Base
from add_default_questions import add_default_questions

engine = create_engine("sqlite:///database.sqlite", echo=True)
main_session = Session(bind=engine)

def setup_db(create_only:bool = False) -> Session:
    Base.metadata.create_all(engine)
    if create_only:
        return main_session
    create_default_users(main_session)
    add_default_questions(main_session)
    return main_session

def create_default_users(session: Session):
    admin_user = User(name="admin", admin=True)
    session.add_all([admin_user])
    session.commit()

if __name__ == "__main__":
    setup_db()