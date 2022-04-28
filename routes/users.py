from flask import Blueprint

users_blueprint = Blueprint("users_blueprint", __name__)


@users_blueprint.route("/", methods=["GET"])
def test():
    return "Hello user!"
