from datetime import datetime

from app import mysql_db as db
from app.main.provider.repository import BaseModel


class CommentReply(BaseModel):
    __bind_key__ = 'mysql_bind'
    __tablename__ = 'comment_reply'

    id = db.Column('id', db.BIGINT, primary_key=True, autoincrement=True)
    comment_id = db.Column('comment_id', db.BIGINT, db.ForeignKey('comment.id'), nullable=False, comment='评论ID')
    reply_type = db.Column('reply_type', db.Integer, nullable=False, comment='评论回复类型，0-针对评论回复，1-针对回复的回复')
    content = db.Column('content', db.Text, nullable=False, comment='评论内容')
    reply_id = db.Column('reply_id', db.BIGINT, nullable=False, comment='回复目标ID')
    uid = db.Column('uid', db.BIGINT, nullable=False, comment='回复人的ID')
    to_uid = db.Column('to_uid', db.BIGINT, nullable=False, comment='回复目标人的ID')
    like = db.Column('like', db.BIGINT, nullable=False, default=0, comment='点赞数量')
    tread = db.Column('tread', db.BIGINT, nullable=False, default=0, comment='踩数量')
    ctime = db.Column('ctime', db.DateTime, nullable=False, default=datetime.now(), comment='创建时间')
    mtime = db.Column('mtime', db.DateTime, nullable=False, default=datetime.now(), comment='更新时间')

    _default_fields = [
        "id",
        "comment_id",
        "reply_type",
        "content",
        "uid",
        "to_uid",
        "like",
        "tread",
        "replys",
        "ctime",
        "mtime"
    ]
