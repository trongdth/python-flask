from flask import Blueprint, request, g
from flask_jwt_extended import (create_access_token, jwt_required, get_jwt_identity, decode_token)
from app import db
from app.helpers.response import response_ok, response_error
from app.helpers.utils import *
from app.helpers.message import MESSAGE, CODE
from app.models import User

import hashlib

user_routes = Blueprint('user', __name__)

@user_routes.route('/login', methods=['POST'])
def login():
    """
    "   user login based on [email] and [password]
    """
    data = request.json
    if data is None:
        return response_error(MESSAGE.INVALID_PARAMETER, CODE.INVALID_PARAMETER)

    email = data['email']
    password = data['password']

    if is_valid_email(email) == False:
        return response_error(MESSAGE.INVALID_EMAIL, CODE.INVALID_EMAIL)

    user = User.find_by_email(email)
    if user is  None:
        return response_error(MESSAGE.USER_NOT_FOUND, CODE.USER_NOT_FOUND)
    
    candidate_password =  hashlib.md5('{}{}'.format(password.strip(), 'appscyclone')).hexdigest()
    hashed_password = user.password

    if hashed_password != candidate_password:
        return response_error(MESSAGE.PASSWORD_NOT_MATCH, CODE.PASSWORD_NOT_MATCH)
    
    return create_access_token('ok')


@user_routes.route('/register', methods=['POST'])
def register():
    """
    "   user register based on [name], [email] and [password]
    """
    try:
        data = request.json
        if data is None:
            return response_error(MESSAGE.INVALID_PARAMETER, CODE.INVALID_PARAMETER)

        email = data['email']
        name = data['name'] 
        password = data['password']

        if is_valid_email(email) == False:
            return response_error(MESSAGE.INVALID_EMAIL, CODE.INVALID_EMAIL)

        user = User.find_by_email(email)
        if user is not None:
            return response_error(MESSAGE.USER_HAS_EMAIL_EXIST_ALREADY, CODE.USER_HAS_EMAIL_EXIST_ALREADY)

        confirm = hashlib.md5('{}{}'.format(password.strip(), 'appscyclone')).hexdigest()
        user = User(
            name=name,
            email=email,
            password=confirm,
        )
        db.session.add(user)
        db.session.commit()

        return response_ok(user.to_json())
    except Exception as ex:
        db.rollback()
        return response_error(str(ex))

