class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///fund_management.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
