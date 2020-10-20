from flask_restx import Api
from flask import Blueprint

from .user import api as users

blueprint = Blueprint("api", __name__)
api = Api(blueprint, title="API", description="description")

# apis
api.add_namespace(users, "/users")