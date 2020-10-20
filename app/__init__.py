from flask import Flask

from config import appConfig
from .extensions import db, migrate

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(appConfig[config_name])

    register_extensions(app)

    migrate.init_app(app, db)
    # from . import models

    from .apis import blueprint
    app.register_blueprint(blueprint)

    return app

def register_extensions(app):
    db.init_app(app)