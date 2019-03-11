from datetime import datetime

from flask import request, jsonify
import logging
from app.main.provider.controller import api
from app.main.provider.utils.return_msg import ReturnMsg
from ..repository.comment import Comment


logger = logging.getLogger(__name__)


@api.route('/comment/create', methods=['GET', 'POST'])
def create_comment():
    if request.method and request.method == 'POST':
        args = request.form
        return_msg = ReturnMsg()
        try:
            comment = Comment()
            comment.aid = args.get('aid', type=int)
            comment.uid = args.get('uid', type=int)
            comment.content = args.get('content')
            comment.like = args.get('like', type=int, default=0)
            comment.tread = args.get('tread', type=int, default=0)
            comment.ctime = datetime.now()
            comment.mtime = datetime.now()
            comment.add()
            return_msg.isSuccess = True
            return_msg.messege = '保存评论成功'
        except Exception as e:
            logger.error('保存评论出现错误')
            return_msg.isSuccess = False
            return_msg.messege = '保存评论出现错误'
        return jsonify(return_msg.__dict__)


@api.route('/comment/addlike', method=['GET', 'POST'])
def add_comment_like():
    


@api.route('/comment/get_list', methods=['GET', 'POST'])
def get_comment_list():
    if request.method and request.method == 'POST':
        args = request.values.to_dict()
    else:
        args = request.args.to_dict()
    return_msg = ReturnMsg()

    id = args.get('id')

    if not id:
        return_msg.isSuccess = False
        return_msg.messege = '缺少参数id'
    else:

        try:
            # 根据ID检索文章
            result = Comment.get_comment_list(id)
            return_msg.messege = '获取评论成功'
            return_msg.isSuccess = True
        except Exception as e:
            logger.error('获取评论失败')
            return_msg.isSuccess = False
            return_msg.messege = '获取评论失败'
        return_msg.result = result
    return jsonify(return_msg.__dict__)
