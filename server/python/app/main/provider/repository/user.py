from app import mysql_db as db


class User(db.Model):
    __bind_key__ = 'mysql_bind'
    __tablename__ = 'user'
    id = db.Column('id', db.BIGINT, primary_key=True, nullable=False, autoincrement=True)
    account = db.Column('account', db.String(255), unique=True, nullable=False, comment='用户名')
    password = db.Column('password', db.String(255), nullable=False, comment='密码')
    nick_name = db.Column('nick_name', db.String(100), nullable=False, comment='昵称')
    role = db.Column('role', db.SmallInteger, nullable=False, default=1, comment='角色')
    avatar = db.Column('avatar', db.BLOB, comment='头像')
    github = db.Column('github', db.String(255), default='')
