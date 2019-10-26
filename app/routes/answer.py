from flask import Blueprint, request, g
from flask_jwt_extended import (create_access_token, jwt_required, get_jwt_identity, decode_token)
from app import db
from app.helpers.response import response_ok, response_error
from app.helpers.utils import *
from app.helpers.message import MESSAGE, CODE
from app.models import Answer

answer_routes = Blueprint('answer', __name__)


@answer_routes.route('/add', methods=['POST'])
def addAnswer():
    try:

        data = request.json

        

        if data is None:
            return response_error(MESSAGE.INVALID_PARAMETER, CODE.INVALID_PARAMETER)


        bm_id = data['bm_id']
        questions = data['question']
        user_id = get_jwt_identity()

        if len(questions) == 0:
            return response_error(MESSAGE.EMPTY_QUESTION, CODE.EMPTY_QUESTION)

        for q in questions:
            answer = Answer(
                bm_id=bm_id,
                answer=q['answer'],
                question_id=q['id'],
                user_id=user_id
            )
            db.session.add(answer)
            db.session.commit()
            
            
        return response_ok()
    except Exception as ex:
        db.session.rollback()
        return response_error(str(ex))

