from flask import Blueprint, request, g
from flask_jwt_extended import (create_access_token, jwt_required, get_jwt_identity, decode_token)
from app import db
from app.helpers.response import response_ok, response_error
from app.helpers.utils import *
from app.helpers.message import MESSAGE, CODE
from app.helpers.decorators import only_admin
from app.models import Question

import hashlib

question_routes = Blueprint('question', __name__)

@question_routes.route('/add', methods=['POST'])
@jwt_required
@only_admin
def add():
    """
    "   add question based on [name]
    """
    try:
        data = request.json
        if data is None:
            return response_error(MESSAGE.INVALID_PARAMETER, CODE.INVALID_PARAMETER)

        name = data['name']
        question = Question(
            name=name,
        )
        db.session.add(question)
        db.session.commit()

        return response_ok(question.to_json())
    except Exception as ex:
        db.rollback()
        return response_error(str(ex))