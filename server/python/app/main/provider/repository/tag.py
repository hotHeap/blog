from datetime import datetime
from app import mysql_db as db
import logging

from . import BaseModel

logger = logging.getLogger(__name__)


class Tag(BaseModel):
    __bind_key__ = 'mysql_bind'
    __tablename__ = 'tag'
    id = db.Column('id', db.BIGINT, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column('name', db.String(100), nullable=False, comment='标签名称')
    ctime = db.Column('ctime', db.DateTime, nullable=False, default=datetime.now(), comment='创建时间')
    mtime = db.Column('mtime', db.DateTime, nullable=False, default=datetime.now(), comment='更新时间')

    _default_fields = [
        'id',
        'name'
    ]

    @staticmethod
    def get_one(id):
        try:
            ret = Tag.query.filter(Tag.id == id).first()
            return ret
        except Exception as e:
            logger.error('获取标签信息出现错误, %s' % e)
            raise Exception('获取标签信息失败')

    @staticmethod
    def get_list(page_index=1, page_size=10):
        try:
            page_inate_datas = Tag.query.order_by(Tag.id.desc()).paginate(page_index, page_size,
                                                                          error_out=False)

            return page_inate_datas
        except Exception as e:
            logger.error('获取标签列表出现错误, %s' % e)
            raise Exception('获取标签列表信息失败')

    def add(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            logger.error('保存标签数据失败, %s' % e)
            raise Exception('保存标签数据失败')

    def update(self):
        try:
            db.session.commit()
        except Exception as e:
            logger.error('更新数据出现错误, %s' % e)
            raise Exception('更新数据失败')

    @staticmethod
    def delete(ids):
        try:
            Tag.query.filter(Tag.id.in_(ids)).delete(synchronize_session=False)
            db.session.commit()
        except Exception as e:
            logger.error('删除数据出现错误, %s' % e)
            raise Exception('删除数据失败')
