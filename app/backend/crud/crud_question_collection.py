from data.database import session
from models import QuestionCollection, Question
from schemas.question_collection import QuestionCollectionRead, QuestionCollectionCreate, QuestionCollectionUpdate
from .base import CRUDHandler

class QuestionCollectionCRUD(CRUDHandler[QuestionCollection, QuestionCollectionRead, QuestionCollectionCreate, QuestionCollectionUpdate]):

    def __init__(self):
        super().__init__("question_collection", session, QuestionCollection, QuestionCollectionRead, QuestionCollectionCreate, QuestionCollectionUpdate)

    def update(self, object_id: int, updated_object: QuestionCollectionUpdate) -> QuestionCollectionRead:
        question_ids = updated_object.question_ids
        del updated_object.question_ids
        if question_ids is not None:
            updated_object.questions = self.session.query(Question).filter(Question.id.in_(question_ids)).all()
        return super().update(object_id, updated_object)

handler: QuestionCollectionCRUD = QuestionCollectionCRUD()