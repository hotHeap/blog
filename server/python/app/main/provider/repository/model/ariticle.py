import logging
from app import sql_db as db

logger = logging.getLogger(__name__)


class Article(db.Model):
    __bind_key__ = 'mysql_bind'
    __tablename__ = 'article'

    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.String(128))
    detail = db.Column('detail', db.String(4000))

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            logger.error('保存数据出现错误, %s' % e)
