import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '012938487yrhstgeWddw^+%&'
    SSL_DISABLE = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    IMAGE_PREFIX = 'http://dilek.co/images/'
    STATIC_DIR = os.path.join(basedir,'static/')
    IMAGE_DIR = STATIC_DIR + 'uploads/'
    IMAGE_RAW_DIR_SUFFIX = 'raw/'
    IMAGE_PROCESSED_DIR_SUFFIX = 'processed/'
    ALLOWED_EXTENSIONS = ['jpg', 'jpeg', 'png', 'gif']
    STATIC_URL_PATH = '/static'

    @staticmethod
    def init_app(app):
      pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    IMAGE_PREFIX = 'http://localhost:5000/static/'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    IMAGE_PREFIX = 'http://dilek.co/images/'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}