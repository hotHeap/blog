import os
from datetime import datetime

from flask import jsonify, request, url_for
import logging

from ..repository.tag import Tag
from app.main.provider.utils.return_msg import ReturnMsg
from . import api

logger = logging.getLogger(__name__)


@api.route('/tag/getList')
def get_tag_list():
    if request.method and request.method == 'POST':
        args = request.values.to_dict()
    else:
        args = request.args.to_dict()

    if 'page' in args:
        page_index = int(args.get('page'))
    else:
        page_index = 1

    if 'pageSize' in args:
        page_size = int(args.get('pageSize'))
    else:
        page_size = 10

    return_msg = ReturnMsg()
    try:
        pagination = Tag.get_list(page_index=page_index, page_size=page_size)

        # 上一页
        prev = None
        if pagination.has_prev:
            prev = url_for('api.get_tag_list', pageIndex=page_index - 1, pageSize=page_size, _external=True)

        # 下一页
        next = None
        if pagination.has_next:
            next = url_for('api.get_tag_list', pageIndex=page_index + 1, pageSize=page_size, _external=True)

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


@api.route('/tag/getOne')
def get_one_tag():
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
        result = Tag.get_one(id)
        return_msg.messege = '获取标签成功'
        return_msg.isSuccess = True
    except Exception as e:
        logger.error('获取标签失败, %s' % e)
        return_msg.isSuccess = False
        return_msg.messege = '获取标签失败'

    return_msg.result = result.to_dict()
    return jsonify(return_msg.__dict__)


@api.route('/tag/create', methods=['GET', 'POST'])
def create_tag():
    '''
        更新文章
    :return:
    '''
    return_msg = ReturnMsg()
    if request.method and request.method == 'POST':
        args = request.values.to_dict()
    else:
        args = request.args.to_dict()

    try:
        tag = Tag()

        tag.name = args.get('name')
        tag.mtime = datetime.now()

        tag.ctime = datetime.now()
        tag.add()
        return_msg.messege = '添加数据成功'

    except Exception as e:
        logger.error('添加数据出现错误, %s' % e)
        return_msg.isSuccess = False
        return_msg.messege = '添加数据错误'

    return jsonify(return_msg.__dict__)


@api.route('/tag/edit')
def edit_tag():
    return_msg = ReturnMsg()
    if request.method and request.method == 'POST':
        args = request.values.to_dict()
    else:
        args = request.args.to_dict()

    if 'id' not in args or 'name' not in args:
        return_msg.isSuccess = False
        return_msg.messege = '参数有误,请检查是否存在参数id, name'
    else:
        try:
            id = args.get('id')
            tag = Tag.get_one(id)

            tag.name = args.get('name')
            tag.update()
            return_msg.isSuccess = True
            return_msg.messege = '修改标签数据成功'
        except Exception as e:
            logger.error('修改标签数据失败, %s' % e)
            return_msg.messege = '修改标签数据失败'

    return jsonify(return_msg.__dict__)


@api.route('/tag/delete')
def delete_tag():
    if request.method and request.method == 'POST':
        args = request.values.to_dict()
    else:
        args = request.args.to_dict()

    # 从request中获取文章id
    ids = args.get('ids')

    return_msg = ReturnMsg()
    if not ids:
        return_msg.messege = '缺少参数id'
        return_msg.isSuccess = False
        return jsonify(return_msg.__dict__)

    try:
        Tag.delete(ids.split(','))
        return_msg.isSuccess = True
        return_msg.messege = '删除数据成功'
    except Exception as e:
        logger.error('获取标签失败, %s' % e)
        return_msg.isSuccess = False
        return_msg.messege = '获取标签失败'

    return jsonify(return_msg.__dict__)
