import os

from flask import Flask
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy

from config import config

current_path = os.path.abspath(os.path.dirname(__file__))

from app.main.provider import Blog

# redis模块
redis_store = FlaskRedis()

# mysql 模块
mysql_db = SQLAlchemy()

# blog 模块
blog_module = Blog()


def create_app(config_name):
    app = Flask(__name__, static_folder=os.path.join(current_path, 'resource'), static_url_path='/7ethan/static')
    app.config.from_object(config[config_name])

    # 注册redis
    redis_store.init_app(app)
    # 注册数据库
    mysql_db.init_app(app)
    create_table(app)
    # 注册blog
    blog_module.init_app(app)
    return app


def create_table(app):
    from app.main.provider.repository.model import Article, Tag, Role, User, Comment, CommentReply

    with app.app_context():
        mysql_db.create_all()
