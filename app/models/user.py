from app import db
from app.models.base import BaseModel
from app.constants import USER_ROLE

class User(BaseModel):

    __tablename__ = 'user'
    __json_public__ = ['name', 'email', 'password']

    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    role_id = db.Column(db.Integer, default="0", server_default="0")

    @classmethod
    def find_by_email(cls, email):
        return User.query.filter(User.email==email).first()

    @classmethod
    def find_by_id(cls, _id):
        return User.query.filter(User.id==_id).first()

    def __repr__(self):
        return '<User {}>'.format(self.id)

