class ReturnMsg(object):
    # 是否成功
    isSuccess = True
    # 返回数据
    result = None
    # 错误码
    errorCode = 0
    # 返回的信息
    messege = None


if __name__ == '__main__':
    import json
    return_msg = ReturnMsg()
    return_msg.result = {
        'a': 1
    }

    print(return_msg.__dict__)
