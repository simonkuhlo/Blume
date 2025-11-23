from sqlalchemy import select
from models import Answer
from database import session
from schemas.answer import AnswerRead, AnswerCreate
from schemas.user import UserRead
from schemas.question import QuestionRead
from schemas.entry import EntryRead

def read_answer(answer_id: int):
    statement = select(Answer).where(Answer.id == answer_id)
    result = session.execute(statement)
    answer = result.scalar()
    print(answer)


def create_answer(answer:AnswerCreate):
    Answer()