from flask_restx import Namespace, Resource, fields

class UserDto:
    api = Namespace("users", description="User API")
    user = api.model(
        "User DTO",
        {
            "email": fields.String
        }
    )
    response = api.model(
        "User Response",
        {
            "status": fields.Boolean,
            "user": fields.Nested(user)
        }
    )

api = UserDto.api
response = UserDto.response

@api.route("")
class Users(Resource):
    @api.doc(
        "",
        response = {
            200: ("Ok", response),
            404: "Not Found"
        }
    )

    def get(self):
        return "wow"
