from flask import Blueprint

blog = Blueprint('blog', __name__)

from app.main.provider.controller import article_controller


class Blog(object):
    def __init__(self, app=None):
        self.app = None
        if app:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        app.register_blueprint(blog, url_prefix='/api')
