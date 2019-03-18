from datetime import datetime
import logging
from app import mysql_db as db
from app.main.provider.repository.article_tag import article_tag
from . import BaseModel
from sqlalchemy.dialects.mysql import BIGINT

logger = logging.getLogger(__name__)


class Article(BaseModel):
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
    comments = db.relationship('Comment')

    tags = db.relationship('Tag', secondary=article_tag, backref=db.backref('articles'))

    _default_fields = [
        "id",
        "uid",
        "title",
        "content",
        "like",
        "tread",
        "view",
        "reply",
        "share",
        "ctime",
        "mtime",
        "tags"
    ]

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            logger.error('保存数据出现错误, %s' % e)
            raise Exception('保存数据失败')

    def update(self):
        try:
            db.session.commit()
        except Exception as e:
            logger.error('更新数据出现错误, %s' % e)
            raise Exception('更新数据失败')

    @staticmethod
    def delete(ids):
        try:
            Article.query.filter(Article.id.in_(ids)).delete(synchronize_session=False)
            db.session.commit()
        except Exception as e:
            logger.error('删除数据出现错误, %s' % e)
            raise Exception('删除数据失败')

    @staticmethod
    def get_article(id):
        try:
            ret = Article.query.filter(Article.id == id).first()
            return ret
        except Exception as e:
            logger.error('获取文章信息出现错误, %s' % e)
            raise Exception('获取文章信息失败')

    @staticmethod
    def get_article_list(page_index=1, page_size=10):
        try:
            page_inate_datas = Article.query.order_by(Article.id.desc()).paginate(page_index, page_size,
                                                                                  error_out=False)

            return page_inate_datas
        except Exception as e:
            logger.error('检索文章列表失败， %s' % e)
            raise Exception('检索文章列表失败')
