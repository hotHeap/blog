from datetime import datetime

from app import mysql_db as db


class Comment(db.Model):
    '''
        评论
    '''
    __bind_key__ = 'mysql_bind'
    __tablename__ = 'comment'

    id = db.Column('id', db.BIGINT, nullable=False, primary_key=True, autoincrement=True)
    uid = db.Column('uid', db.BIGINT, nullable=False, comment='评论人ID')
    type = db.Column('type', db.Integer, nullable=False, default=0, comment='评论类型，0-评论文章，1-评论回复')
    content = db.Column('content', db.TEXT, nullable=False, comment='评论内容')
    like = db.Column('like', db.BIGINT, nullable=False, default=0, comment='点赞数量')
    tread = db.Column('tread', db.BIGINT, nullable=False, default=0, comment='踩数量')
    ctime = db.Column('ctime', db.DateTime, nullable=False, default=datetime.now(), comment='创建时间')
    mtime = db.Column('mtime', db.DateTime, nullable=False, default=datetime.now(), comment='更新时间')
