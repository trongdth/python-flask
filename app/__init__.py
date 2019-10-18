from flask import Flask, g, redirect, request
from app.core import db, jwt, configure_app
from flask_cors import CORS
from models import *
from app.helpers.response import response_error
from app.routes import init_routes
from datetime import datetime

import time
import decimal
import flask.json
import logging, logging.config, yaml

class MyJSONEncoder(flask.json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            # Convert decimal instances to strings.
            return str(float(obj))
        return super(MyJSONEncoder, self).default(obj)


app = Flask(__name__)

logging.config.dictConfig(yaml.load(open('logging.conf')))
logfile = logging.getLogger('file')

# add json encoder for decimal type
app.json_encoder = MyJSONEncoder
# disable strict_slashes
app.url_map.strict_slashes = False
# config app
configure_app(app)

# Accept CORS
# CORS(app)
# init db
db.init_app(app)
# init jwt
jwt.init_app(app)


@app.before_request
def before_request():
	rp = request.path
	if rp != '/' and rp.endswith('/'):
		return redirect(rp[:-1])
	g.PASSPHASE = app.config.get('PASSPHASE')


@app.after_request
def after_request(response):
	if 'start' in g:
		start, url = g.start
		end = time.time()
		diff = end - float(start)
		logfile.debug("API -> {}, time -> {}".format(url, str(diff)))

	return response


init_routes(app)


def jwt_error_handler(message):
	return response_error(message)


def needs_fresh_token_callback():
	return response_error('Only fresh tokens are allowed')


def revoked_token_callback():
	return response_error('Token has been revoked')


def expired_token_callback():
	return response_error('Token has expired', 401)


jwt.unauthorized_loader(jwt_error_handler)
jwt.invalid_token_loader(jwt_error_handler)
jwt.claims_verification_loader(jwt_error_handler)
jwt.token_in_blacklist_loader(jwt_error_handler)
jwt.user_loader_error_loader(jwt_error_handler)
jwt.claims_verification_failed_loader(jwt_error_handler)
jwt.expired_token_loader(expired_token_callback)
jwt.needs_fresh_token_loader(needs_fresh_token_callback)
jwt.revoked_token_loader(revoked_token_callback)


@app.errorhandler(Exception)
def error_handler(err):
	return response_error(err.message)

# @app.errorhandler(404)
# def error_handler400(err):
#   return response_error(err.message);
#
# @app.errorhandler(500)
# def error_handler500(err):
#   return response_error(err.message);
#
# @app.error_handler_all(Exception)
# def errorhandler(err):
#   return response_error(err.message);
