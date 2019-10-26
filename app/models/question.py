from app import db
from app.models.base import BaseModel

class Question(BaseModel):

    __tablename__ = 'question'
    __json_public__ = ['name']

    name = db.Column(db.String(255))

    def __repr__(self):
        return '<Question {}>'.format(self.id)