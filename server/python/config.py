class DevelopConfig(object):
    DEBUG = True
    # redis 配置
    REDIS_URI = 'redis://:password@localhost:6379/0'

    # SQL 配置
    SQLALCHEMY_BINDS = {
        'mysql_bind': 'mysql+pymysql://username:password@localhost/my_blog?charset=utf8mb4'
    }
    pass


class ProductConfig(object):
    DEBUG = False

    # redis 配置
    REDIS_URI = 'redis://:my_redis@localhost:6379/0'

    # SQL 配置
    SQLALCHEMY_BINDS = {
        'mysql_bind': 'mysql+pymysql://root:chenmoru@localhost/my_blog?charset=utf8mb4'
    }
    pass


config = {
    'develop': DevelopConfig,
    'product': ProductConfig,
    'default': DevelopConfig
}

