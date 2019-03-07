from flask import jsonify
import logging

from app.main.provider.utils.return_msg import ReturnMsg
from . import article

logger = logging.getLogger(__name__)


@article.route('/getList', methods=['GET', 'POST'])
def get_list():
    '''
        获取文章列表
    :return:
    '''
    return_msg = ReturnMsg()

    return_msg.messege = 'sucess'
    return_msg.result = {}
    return jsonify(return_msg.__dict__)


@article.route('/getAdminList', methods=['GET', 'POST'])
def get_admin_list():
    '''
        后台获取文章列表
    :return:
    '''
    return_msg = ReturnMsg()

    return_msg.messege = 'sucess'
    return_msg.result = {}
    return jsonify(return_msg.__dict__)


@article.route('/getOne', methods=['GET', 'POST'])
def get_one():
    '''
        获取文章
    :return:
    '''
    return_msg = ReturnMsg()

    return_msg.messege = 'sucess'
    return_msg.result = {}
    return jsonify(return_msg.__dict__)


@article.route('/getPreOrNext', methods=['GET', 'POST'])
def get_pre_next():
    '''
        获取上一篇和下一篇文章
    :return:
    '''
    return_msg = ReturnMsg()

    return_msg.messege = 'sucess'
    return_msg.result = {}
    return jsonify(return_msg.__dict__)


@article.route('/getAdminOne', methods=['GET', 'POST'])
def get_admin_one():
    '''
        后台获取文章
    :return:
    '''
    return_msg = ReturnMsg()

    return_msg.messege = 'sucess'
    return_msg.result = {}
    return jsonify(return_msg.__dict__)


@article.route('/update', methods=['GET', 'POST'])
def update():
    '''
        更新文章
    :return:
    '''
    return_msg = ReturnMsg()

    return_msg.messege = 'sucess'
    return_msg.result = {}
    return jsonify(return_msg.__dict__)


@article.route('/save', methods=['GET', 'POST'])
def save():
    '''
        保存文章
    :return:
    '''
    return_msg = ReturnMsg()

    return_msg.messege = 'sucess'
    return_msg.result = {}
    return jsonify(return_msg.__dict__)


@article.route('/delete', methods=['GET', 'POST'])
def delete():
    '''
        删除文章
    :return:
    '''
    return_msg = ReturnMsg()

    return_msg.messege = 'sucess'
    return_msg.result = {}
    return jsonify(return_msg.__dict__)


@article.route('/updateLove')
def update_love():
    '''
        更新文章的喜欢字段
    :return:
    '''
    return_msg = ReturnMsg()

    return_msg.messege = 'sucess'
    return_msg.result = {}
    return jsonify(return_msg.__dict__)


@article.route('/search')
def search():
    '''
        检索文章
    :return:
    '''
    return_msg = ReturnMsg()

    return_msg.messege = 'sucess'
    return_msg.result = {}
    return jsonify(return_msg.__dict__)


@article.route('/save_db')
def save_db():
    from app.main.provider.repository.model.ariticle import Article

    article = Article()
    article.title = '测试'
    article.content = 'hello world'
    article.uid = '1'
    article.tag = 1
    article.save()

    return_msg = ReturnMsg()

    return_msg.messege = 'sucess'
    return_msg.result = {}
    return jsonify(return_msg.__dict__)


@article.route('/save_redis')
def save_redis():
    from app import redis_store

    redis_store.set('test', 'cmr')
    return_msg = ReturnMsg()

    return_msg.messege = 'sucess'
    return_msg.result = {}
    return jsonify(return_msg.__dict__)
