from app.main.provider.controller.article import Article

article_module = Article()


class Blog(object):
    def __init__(self, app=None):
        self.app = None
        if app:
            self.init_app(app)

    def init_app(self, app):
        self.app = app

        article_module.init_app(app)
