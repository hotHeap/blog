from datetime import datetime
import logging
from app import mysql_db as db
from app.main.provider.repository import BaseModel

logger = logging.getLogger(__name__)


class Comment(BaseModel):
    '''
        评论
    '''
    __bind_key__ = 'mysql_bind'
    __tablename__ = 'comment'

    id = db.Column('id', db.BIGINT, nullable=False, primary_key=True, autoincrement=True)
    aid = db.Column('aid', db.BIGINT, db.ForeignKey('article.id'), nullable=False, comment='文章ID')
    uid = db.Column('uid', db.BIGINT, nullable=False, comment='评论人ID')
    content = db.Column('content', db.TEXT, nullable=False, comment='评论内容')
    like = db.Column('like', db.BIGINT, nullable=False, default=0, comment='点赞数量')
    tread = db.Column('tread', db.BIGINT, nullable=False, default=0, comment='踩数量')
    ctime = db.Column('ctime', db.DateTime, nullable=False, default=datetime.now(), comment='创建时间')
    mtime = db.Column('mtime', db.DateTime, nullable=False, default=datetime.now(), comment='更新时间')
    replys = db.relationship('CommentReply')

    _default_fields = [
        "id",
        "content",
        "like",
        "tread",
        "replys",
        "ctime",
        "mtime"
    ]

    def add(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            logger.error('保存评论出现错误, %s' % e)
            raise Exception('保存评论出现错误')

    @staticmethod
    def get_comment_list(id):
        try:
            results = Comment.query.filter(Comment.aid == id).all()

            return [result.to_dict() for result in results]
        except Exception as e:
            print(e)
            logger.error('检索数据出现错误， %s' % e)
            raise Exception('检索数据出现错误')
