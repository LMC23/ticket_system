from flask import Blueprint, request
import psycopg2.errorcodes
import logging

# import bcrypt

from database import db_class
from dotenv import dotenv_values

logging.basicConfig(filename="app.log", filemode="a", format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

auth_blueprint = Blueprint("auth_blueprint", __name__)

config = dotenv_values(".env")

CONFIG = {
    "HOSTNAME": config.get("DB_HOSTNAME"),
    "DATABASE": config.get("DATABASE"),
    "USERNAME": config.get("DB_USERNAME"),
    "PASSWORD": config.get("DB_PASSWORD"),
    "PORT_ID": config.get("DB_PORT_ID"),
}

db = db_class.Database(CONFIG)


@auth_blueprint.route("/register", methods=["POST"])
def register():
    try:
        user_input = request.json
        first_name = user_input.get("first_name")
        last_name = user_input.get("last_name")
        email = user_input.get("email")

        if first_name is None:
            return {"error": "First name must not be empty."}
        if last_name is None:
            return {"error": "Last name must not be empty."}
        if email is None:
            return {"error": "Email must not be empty."}

        # To do:
        # generate password and username for user
        # save user into db
        # send credentials to user

        # db.insert_user(name, email, password)
        # logger.info(f"User {name} has been successfully created.")
        # return {"message": "User created successfully."}

        return {"first_name": first_name, "last_name": last_name, "email": email}

    except psycopg2.IntegrityError as e:
        if e.pgcode == psycopg2.errorcodes.UNIQUE_VIOLATION:
            logger.error(f"An error has occurred {str(e)}")
            return {"error": "Values must be unique."}

    except Exception as e:
        error = str(e)
        logger.error(f"User could not be created due to {error}")
        return {"error": error}
