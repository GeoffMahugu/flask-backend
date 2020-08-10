class BaseConfig():
    API_PREFIX = '/api'
    TESTING = False
    DEBUG = False


class DevConfig(BaseConfig):
    FLASK_ENV = 'dev'
    DEBUG = True


class ProductionConfig(BaseConfig):
    FLASK_ENV = 'prod'
