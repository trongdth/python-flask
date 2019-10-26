from flask import Blueprint, request, g
from flask_jwt_extended import (create_access_token, jwt_required, get_jwt_identity, decode_token)
from app import db
from app.helpers.response import response_ok, response_error
from app.helpers.utils import *
from app.helpers.message import MESSAGE, CODE
from app.helpers.decorators import only_admin
from app.models import BusinessModel

import hashlib

business_model_routes = Blueprint('business_model', __name__)

@business_model_routes.route('/add', methods=['POST'])
@jwt_required
def add():
    """
    "   add business model based on [name]
    """
    try:
        data = request.json
        if data is None:
            return response_error(MESSAGE.INVALID_PARAMETER, CODE.INVALID_PARAMETER)

        name = data['name']
        bm = BusinessModel(
            name=name,
        )
        db.session.add(bm)
        db.session.commit()

        return response_ok(bm.to_json())
    except Exception as ex:
        db.rollback()
        return response_error(str(ex))


@business_model_routes.route('/list', methods=['GET']) 
@jwt_required 
def list_business_model():

    bms = BusinessModel.query.all()

    arr = []
    for bm in bms:
        arr.append(bm.to_json())

    return response_ok(arr) 
