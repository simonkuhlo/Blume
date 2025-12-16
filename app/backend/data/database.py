from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine, Engine, event
from sqlite3 import Connection as SQLite3Connection
from sqlalchemy.orm import Session

@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()

engine = create_engine("sqlite:///data/database.sqlite", echo=True)
session = Session(bind=engine)