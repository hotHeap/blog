import os

from flask import request, jsonify

from app.main.provider.utils.return_msg import ReturnMsg
from . import api


@api.route('/upload', methods=['POST'])
def upload():
    return_msg = ReturnMsg()
    if request.method and request.method == 'POST':
        if 'file' not in request.files:
            return_msg.isSuccess = False
            return_msg.messege = '上传文件不能为空'
            return jsonify(return_msg.__dict__)
        file = request.files['file']

        if not file:
            return_msg.isSuccess = False
            return_msg.messege = '上传文件不能为空'
            return jsonify(return_msg.__dict__)

        filename = file.filename

        upload_path = os.path.join(os.getcwd(), 'app/static/uploads')
        file_path = os.path.join(upload_path, filename)
        file.save(file_path)

        return_msg.isSuccess = True
        return_msg.messege = '文件上传成功'
        return_msg.result = os.path.join('/static/uploads', filename)

        return jsonify(return_msg.__dict__)
    return_msg.isSuccess = False
    return_msg.messege = '文件上传失败'
    return jsonify(return_msg.__dict__)
