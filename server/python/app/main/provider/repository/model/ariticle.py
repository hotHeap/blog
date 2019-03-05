from datetime import datetime
import logging
from app import mysql_db as db
from sqlalchemy.dialects.mysql import BIGINT
logger = logging.getLogger(__name__)


class Article(db.Model):
    __bind_key__ = 'mysql_bind'
    __tablename__ = 'article'

    id = db.Column('id', db.BIGINT, primary_key=True, nullable=False, autoincrement=True)
    uid = db.Column('uid', db.BIGINT, nullable=False, comment='作者')
    title = db.Column('title', db.String(225), nullable=False, comment='文章标题')
    content = db.Column('content', db.Text, nullable=False, comment='文章内容')
    like = db.Column('like', db.Integer, nullable=False, default=0, comment='点赞数')
    tread = db.Column('tread', db.BIGINT, nullable=False, default=0, comment='踩数量')
    view = db.Column('view', BIGINT(unsigned=True), nullable=False, default=0, comment='浏览次数')
    reply = db.Column('reply', BIGINT(unsigned=True), nullable=False, default=0, comment='回复数')
    share = db.Column('share', BIGINT(unsigned=True), nullable=False, default=0, comment='分享次数')
    ctime = db.Column('ctime', db.DateTime, nullable=False, default=datetime.now())
    mtime = db.Column('mtime', db.DateTime, nullable=False, default=datetime.now())
    tag = db.Column('tag', db.Integer, nullable=False, comment='文章标签')

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            logger.error('保存数据出现错误, %s' % e)
