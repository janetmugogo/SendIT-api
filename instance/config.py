import os
JWT_SECRET_KEY = 'jwt-secret-string'

class Config(object):
    #parent configuration class
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    DATABASE_URI = os.getenv('DATABASE_URL')

class DevelopmentConfig(Config):
    # configuration for development
    TESTING = True
    DATABASE_URI = os.getenv('DATABASE_DEVELOPMENT')
    DEBUG = True

class TestingConfig(Config):
    #configuration for testing db
    TESTING = True
    DATABASE_URI = os.getenv('DATABASE_TESTING')
    DEBUG = True

class ProductionConfig(Config):
    #Configurations for Production
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}

