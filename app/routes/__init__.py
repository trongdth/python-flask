from flask import request, g


def init_routes(app):
    
    @app.route('/')
    def hello():
        return 'API'