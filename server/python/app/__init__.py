import os

from flask import Flask
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy

current_path = os.path.abspath(os.path.dirname(__file__))

# redis模块
redis_store = FlaskRedis()

# mysql 模块
mysql_db = SQLAlchemy()

# blog 模块
from app.main.provider.repository import Article, Tag, Role, User, Comment, CommentReply, article_tag


def create_app(config_name):
    app = Flask(__name__, static_folder=os.path.join(current_path, 'static'), static_url_path='/static')
    app.config.from_pyfile(os.path.join(os.getcwd(), config_name))

    # 注册redis
    redis_store.init_app(app)
    # 注册数据库
    mysql_db.init_app(app)
    create_table(app)

    from .main.provider.controller import api
    app.register_blueprint(api, url_prefix='/api')

    return app


def create_table(app):
    with app.app_context():
        mysql_db.create_all()
