from flask import request, g
from app.routes.user import user_routes
from app.routes.question import question_routes
from app.routes.business_model import business_model_routes
from app.routes.answer import answer_routes

def init_routes(app):
    
    @app.route('/')
    def hello():
        return 'API'

    app.register_blueprint(user_routes)
    app.register_blueprint(question_routes, url_prefix='/question')
    app.register_blueprint(business_model_routes, url_prefix='/business-model')
    app.register_blueprint(answer_routes, url_prefix='/answer')
    

    