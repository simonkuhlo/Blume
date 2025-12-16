from models import QuestionCollection, Question
from schemas.question_collection import QuestionCollectionRead
from ..database import session


def modify_questions_of_collection(question_collection_id: int, question_id:int, remove: bool = False) -> QuestionCollectionRead:
    collection = session.query(QuestionCollection).filter(QuestionCollection.id == question_collection_id).first()
    question = session.query(Question).filter(Question.id == question_id).first()
    if remove:
        collection.questions.remove(question)
    else:
        collection.questions.append(question)
    session.commit()
    session.refresh(collection)
    return QuestionCollectionRead.model_validate(collection)