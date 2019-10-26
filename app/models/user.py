from app import db
from app.models.base import BaseModel

class User(BaseModel):

    __tablename__ = 'user'
    __json_public__ = ['name', 'email', 'password']

    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))

    @classmethod
    def find_by_email(cls, email):
        return User.query.filter(User.email==email).first()

    def __repr__(self):
        return '<User {}>'.format(self.id)

