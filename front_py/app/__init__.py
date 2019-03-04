import os

from flask import Flask

from config import config

current_path = os.path.abspath(os.path.dirname(__file__))

from app.main.provider import Blog

blog_module = Blog()


def create_app(config_name):
    app = Flask(__name__, static_folder=os.path.join(current_path, 'resource'), static_url_path='/7ethan/static')
    app.config.from_object(config[config_name])

    # 注册blog
    blog_module.init_app(app)
    return app
