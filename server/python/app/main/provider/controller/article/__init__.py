from flask import Blueprint

article = Blueprint('article', __name__)

from . import article_controller


class Article(object):
    def __init__(self, app=None):
        self.app = None
        if app:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        app.register_blueprint(article, url_prefix='/api/article')
