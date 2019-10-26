from app import db
from app.models.base import BaseModel

class Question(BaseModel):

    __tablename__ = 'question'
    __json_public__ = ['id','name']

    name = db.Column(db.String(255))

    @classmethod
    def get_list_question(cls):
        return Question.query.all()

    def __repr__(self):
        return '<Question {}>'.format(self.id)