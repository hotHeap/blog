from datetime import datetime
from app import mysql_db as db


class Tag(db.Model):
    __bind_key__ = 'mysql_bind'
    __tablename__ = 'tag'
    id = db.Column('id', db.BIGINT, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column('name', db.String(100), nullable=False, comment='标签名称')
    ctime = db.Column('ctime', db.DateTime, nullable=False, default=datetime.now(), comment='创建时间')
    mtime = db.Column('mtime', db.DateTime, nullable=False, default=datetime.now(), comment='更新时间')
