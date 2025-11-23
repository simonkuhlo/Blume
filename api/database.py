from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

class Base(DeclarativeBase):
    pass

def setup_db():
    Base.metadata.create_all(engine)

engine = create_engine("sqlite:///database.sqlite", echo=True)
session = Session(bind=engine)