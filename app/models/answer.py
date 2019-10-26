from app import db
from app.models.base import BaseModel

class Answer(BaseModel):

    __tablename__ = 'answer'
    __json_public__ = ['id', 'name']

    answer = db.Column(db.Text)
    user_id = db.Column('user_id', db.ForeignKey('user.id'))
    bm_id = db.Column('bm_id', db.ForeignKey('business_model.id'))
    question_id = db.Column('question_id', db.ForeignKey('question.id'))

    def __repr__(self):
        return '<Answer {}>'.format(self.id)