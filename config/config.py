import os

# from config.utils import getConfig
# from config import CONFIG_PATH, FLASK_ENV

# from app.model.user import User


BASE_DIR = os.path.dirname(__file__)
# https://github.com/X1Zeth2X/flask-restx-boilerplate/blob/master/config.py


# CONSTANT = getConfig(CONFIG_PATH, FLASK_ENV)

class Config:
    DEBUG = False


class LocalConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(os.path.join(BASE_DIR, "my.db"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(os.path.join(BASE_DIR, "my.db"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False


appConfig = dict(
    local=LocalConfig,
    dev=DevConfig,
    prod=ProdConfig,
)
