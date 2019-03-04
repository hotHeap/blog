from flask import jsonify
import logging
from app.main.provider.utils.return_msg import ReturnMsg
from app.main.provider import blog

logger = logging.getLogger(__name__)


@blog.route('/article/getList', methods=['GET', 'POST'])
def get_list():
    '''
        获取文章列表
    :return:
    '''
    return_msg = ReturnMsg()

    return_msg.messege = 'sucess'
    return_msg.result = {}
    return jsonify(return_msg.__dict__)


@blog.route('/article/getAdminList', methods=['GET', 'POST'])
def get_admin_list():
    '''
        后台获取文章列表
    :return:
    '''
    return_msg = ReturnMsg()

    return_msg.messege = 'sucess'
    return_msg.result = {}
    return jsonify(return_msg.__dict__)


@blog.route('/article/getOne', methods=['GET', 'POST'])
def get_one():
    '''
        获取文章
    :return:
    '''
    return_msg = ReturnMsg()

    return_msg.messege = 'sucess'
    return_msg.result = {}
    return jsonify(return_msg.__dict__)


@blog.route('/article/getPreOrNext', methods=['GET', 'POST'])
def get_pre_next():
    '''
        获取上一篇和下一篇文章
    :return:
    '''
    return_msg = ReturnMsg()

    return_msg.messege = 'sucess'
    return_msg.result = {}
    return jsonify(return_msg.__dict__)


@blog.route('/article/getAdminOne', methods=['GET', 'POST'])
def get_admin_one():
    '''
        后台获取文章
    :return:
    '''
    return_msg = ReturnMsg()

    return_msg.messege = 'sucess'
    return_msg.result = {}
    return jsonify(return_msg.__dict__)


@blog.route('/article/update', methods=['GET', 'POST'])
def update():
    '''
        更新文章
    :return:
    '''
    return_msg = ReturnMsg()

    return_msg.messege = 'sucess'
    return_msg.result = {}
    return jsonify(return_msg.__dict__)


@blog.route('/article/save', methods=['GET', 'POST'])
def save():
    '''
        保存文章
    :return:
    '''
    return_msg = ReturnMsg()

    return_msg.messege = 'sucess'
    return_msg.result = {}
    return jsonify(return_msg.__dict__)


@blog.route('/article/delete', methods=['GET', 'POST'])
def delete():
    '''
        删除文章
    :return:
    '''
    return_msg = ReturnMsg()

    return_msg.messege = 'sucess'
    return_msg.result = {}
    return jsonify(return_msg.__dict__)


@blog.route('/article/updateLove')
def update_love():
    '''
        更新文章的喜欢字段
    :return:
    '''
    return_msg = ReturnMsg()

    return_msg.messege = 'sucess'
    return_msg.result = {}
    return jsonify(return_msg.__dict__)


@blog.route('/article/search')
def search():
    '''
        检索文章
    :return:
    '''
    return_msg = ReturnMsg()

    return_msg.messege = 'sucess'
    return_msg.result = {}
    return jsonify(return_msg.__dict__)
