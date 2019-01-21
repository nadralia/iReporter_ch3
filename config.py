class Config(object):
    """
    Common configurations
    """
    SECRET_KEY = 'mysecretkey'
    JWT_ACCESS_TOKEN_EXPIRES = False
    JWT_TOKEN_LOCATION = ['headers']
    JWT_HEADER_NAME = 'Authorization'
    JWT_HEADER_TYPE = 'Bearer'
    DEBUG = False


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True


class TestingConfig(Config):
    """
    Testing application configuration
    """
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
