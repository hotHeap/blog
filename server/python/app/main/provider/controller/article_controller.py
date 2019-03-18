import os
from datetime import datetime

from flask import jsonify, request, url_for
import logging

from app.main.provider.utils.markdown import markdown_to_html
from . import api
from app.main.provider.utils.return_msg import ReturnMsg
from ..repository.ariticle import Article
from ..repository.tag import Tag


logger = logging.getLogger(__name__)


@api.route('/article/getList', methods=['GET', 'POST'])
def get_article_list():
    '''
        获取文章列表
    :return:
    '''

    if request.method and request.method == 'POST':
        args = request.values.to_dict()
    else:
        args = request.args.to_dict()

    page_index = args.get('page')

    if page_index:
        page_index = int(page_index)

    page_size = args.get('pageSize')
    if page_size:
        page_size = int(page_size)


    return_msg = ReturnMsg()
    try:
        pagination = Article.get_article_list(page_index=page_index, page_size=page_size)

        # 上一页
        prev = None
        if pagination.has_prev:
            prev = url_for('api.get_article_list', pageIndex=page_index - 1, pageSize=page_size, _external=True)

        # 下一页
        next = None
        if pagination.has_next:
            next = url_for('api.get_article_list', pageIndex=page_index + 1, pageSize=page_size, _external=True)

        return_msg.messege = 'sucess'
        return_msg.result = {
            'data': [article.to_dict() for article in pagination.items],
            'prev': prev,
            'next': next,
            'total': pagination.total,
            'pages': pagination.pages
        }
    except Exception as e:
        logger.error('获取文章列表出现错误, %s' % e)
        return_msg.isSuccess = False
        return_msg.messege = '获取文章列表失败'
    return jsonify(return_msg.__dict__)


@api.route('/article/getOne', methods=['GET', 'POST'])
def get_one():
    '''
        获取文章
    :return:
    '''
    if request.method and request.method == 'POST':
        args = request.values.to_dict()
    else:
        args = request.args.to_dict()

    # 从request中获取文章id
    id = args.get('id')

    return_msg = ReturnMsg()
    if not id:
        return_msg.messege = '缺少参数id'
        return_msg.isSuccess = False
        return jsonify(return_msg.__dict__)

    try:
        # 根据ID检索文章
        result = Article.get_article(id)
        return_msg.messege = '获取文章成功'
        return_msg.isSuccess = True
    except Exception as e:
        logger.error('获取文章失败')
        return_msg.isSuccess = False
        return_msg.messege = '获取文章失败'

    return_msg.result = result.to_dict()
    return jsonify(return_msg.__dict__)


@api.route('/article/create', methods=['POST'])
def create():
    '''
        更新文章
    :return:
    '''
    return_msg = ReturnMsg()
    if request.method and request.method == 'POST':
        try:
            args = request.form
            article = Article()

            article.uid = args.get('uid')
            article.title = args.get('title')
            article.content = args.get('content')
            article.like = args.get('like', type=int, default=0)
            article.tread = args.get('tread', type=int, default=0)
            article.view = args.get('view', type=int, default=0)
            article.reply = args.get('reply', type=int, default=0)
            article.share = args.get('share', type=int, default=0)

            article.ctime = datetime.now()
            article.mtime = datetime.now()

            tag = Tag()
            tag_id = args.get('tag_id')
            if tag_id:
                tag.id = tag_id
            tag.name = args.get('tag_name')
            article.tags.append(tag)
            article.save()
            return_msg.messege = '添加数据成功'

        except Exception as e:
            logger.error('添加数据出现错误, %s' % e)
            return_msg.isSuccess = False
            return_msg.messege = '添加数据错误'

    return jsonify(return_msg.__dict__)


@api.route('/article/edit', methods=['GET', 'POST'])
def edit():
    return_msg = ReturnMsg()
    if request.method and request.method == 'POST':
        args = request.values.to_dict()
    else:
        args = request.args.to_dict()

    try:
        id = args.get('id', type='int')
        article = Article.get_article(id)
        article.uid = args.get('uid')
        article.title = args.get('title')
        article.content = args.get('content')
        article.like = args.get('like')
        article.tread = args.get('tread')
        article.view = args.get('view')
        article.reply = args.get('reply', type='int', default=0)
        article.share = args.get('share', type='int', default=0)
        article.mtime = datetime.now()

        Tag

        article.update()
    except Exception as e:
        logger.error('更新文章出现错误, %s' % e)
        return_msg.isSuccess = False
        return_msg.messege = '更新文章错误'

    return jsonify(return_msg.__dict__)


@api.route('/article/delete', methods=['GET', 'POST'])
def delete():
    '''
        删除文章
    :return:
    '''
    if request.method and request.method == 'POST':
        args = request.values.to_dict()
    else:
        args = request.args.to_dict()
    return_msg = ReturnMsg()

    ids = args.get('ids')
    try:
        Article.delete(ids.split(','))
        return_msg.messege = '删除文章成功'
    except Exception as e:
        logger.error(e)
        return_msg.isSuccess = False
        return_msg.messege = '删除文章失败'

    return jsonify(return_msg.__dict__)


@api.route('/article/updateLove')
def update_love():
    '''
        更新文章的喜欢字段
    :return:
    '''
    return_msg = ReturnMsg()

    return_msg.messege = 'sucess'
    return_msg.result = {}
    return jsonify(return_msg.__dict__)


@api.route('/article/detail/<int:id>')
def detail(id):
    return_msg = ReturnMsg()

    article = Article.get_article(id)

    return_msg.messege = 'sucess'
    return_msg.result = article
    return jsonify(return_msg.__dict__)


@api.route('/article/search')
def search():
    '''
        检索文章
    :return:
    '''
    return_msg = ReturnMsg()

    return_msg.messege = 'sucess'
    return_msg.result = {}
    return jsonify(return_msg.__dict__)





@api.route('/test')
def test():
    file = 'README.md'
    html = markdown_to_html(os.path.join(os.getcwd(), 'app/static/uploads', file))
    return html
