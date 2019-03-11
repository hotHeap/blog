from app import mysql_db as db

article_tag = db.Table(
    'article_tag',
    db.Column('article_id', db.BIGINT, db.ForeignKey('article.id'), primary_key=True),
    db.Column('tag_id', db.BIGINT, db.ForeignKey('tag.id'), primary_key=True),
    extend_existing=True,
    info={'bind_key': 'mysql_bind'}
)
