from datetime import datetime

from app import mysql_db as db
from sqlalchemy.dialects.mysql import BIGINT


class Role(db.Model):
    __bind_key__ = 'mysql_bind'
    __tablename__ = 'role'

    id = db.Column('id', BIGINT(unsigned=True), nullable=False, autoincrement=True, primary_key=True)
    name = db.Column('name', db.String(128), nullable=False, comment='角色名称')
    op_user = db.Column('op_user', db.BIGINT, nullable=False, comment='操作人')
    ctime = db.Column('ctime', db.DateTime, nullable=False, default=datetime.now(), comment='创建时间')
    mtime = db.Column('mtime', db.DateTime, nullable=False, default=datetime.now(), comment='更新时间')
