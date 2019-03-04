class DevelopConfig(object):
    DEBUG = True
    pass


class ProductConfig(object):
    DEBUG = False
    pass


config = {
    'develop': DevelopConfig,
    'product': ProductConfig,
    'default': DevelopConfig
}

