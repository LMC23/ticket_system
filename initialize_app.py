from database import db_class
from dotenv import dotenv_values

config = dotenv_values(".env")

CONFIG = {
    "HOSTNAME": config.get("DB_HOSTNAME"),
    "DATABASE": config.get("DATABASE"),
    "USERNAME": config.get("DB_USERNAME"),
    "PASSWORD": config.get("DB_PASSWORD"),
    "PORT_ID": config.get("DB_PORT_ID"),
}

try:
    db = db_class.Database(CONFIG)
    drop_query = "DROP TABLE IF EXISTS users"
    drop_table = db.execute_query(drop_query)

    table_template = """ CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                first_name text NOT NULL,
                last_name text NOT NULL,
                email text UNIQUE NOT NULL,
                username text UNIQUE NOT NULL,
                password text NOT NULL,
                role text NOT NULL DEFAULT 'USER'
            )
            """
    create_table = db.execute_query(table_template)
    print(create_table)
except Exception as error:
    print(error)
