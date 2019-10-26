from flask import request, g
from app.routes.user import user_routes

def init_routes(app):
    
    @app.route('/')
    def hello():
        return 'API'

    app.register_blueprint(user_routes)