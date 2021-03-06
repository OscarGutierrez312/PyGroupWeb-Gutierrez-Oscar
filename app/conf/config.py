
class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///shop.sqlite3"
    SQLALCHEMY_TRACK_MODIFICATION = False
    SECRET_KEY = 'any secret string'  

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/foo'
    


class DevelopmentConfig(Config):
    DEBUG = True
    
    

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///testdb.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATION = True
    DB_USERNAME = 'test'
    DB_PASSWORD = 'test-pass'
    WTF_CSRF_ENABLED = False