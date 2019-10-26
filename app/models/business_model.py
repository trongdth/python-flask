from app import db
from app.models.base import BaseModel

class BusinessModel(BaseModel):

    __tablename__ = 'business_model'
    __json_public__ = ['id', 'name']

    name = db.Column(db.String(255))

    def __repr__(self):
        return '<BusinessModel {}>'.format(self.id)