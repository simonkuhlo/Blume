from sqlalchemy import Column
from sqlalchemy import Table
from database import Base
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship

association_table = Table("collection_has_questions",
                          Base.metadata,
                          Column("collection_id", Integer, ForeignKey("question_collection.id")),
                          Column("question_id", Integer, ForeignKey("question.id"))
                          )