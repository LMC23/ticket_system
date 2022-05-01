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


def drop_table(db, table):
    try:
        drop_query = f"DROP TABLE IF EXISTS {table};"
        db.execute_query(drop_query)
        print(f"Table {table} successfully deleted.")
    except Exception as e:
        raise e


def drop_all_tables(db):
    try:
        drop_table(db, "ticket_logs")
        drop_table(db, "ticket")
        drop_table(db, "ticket_type")
        drop_table(db, "users")
        drop_table(db, "priority")
        drop_table(db, "status")
        drop_table(db, "category")
    except Exception as error:
        print(error)


def create_user_table(db):
    try:
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
        db.execute_query(table_template)
        print("Users table created.")
    except Exception as error:
        print(error)


def create_priority_table(db):
    try:
        table_template = """ CREATE TABLE IF NOT EXISTS priority (
                    id SERIAL PRIMARY KEY,
                    level text NOT NULL
        )
        """
        db.execute_query(table_template)
        print("Priority table created.")
    except Exception as error:
        print(error)


def create_status_table(db):
    try:
        table_template = """ CREATE TABLE IF NOT EXISTS status (
                    id SERIAL PRIMARY KEY,
                    status text NOT NULL
        )
        """
        db.execute_query(table_template)
        print("Status table created.")
    except Exception as error:
        print(error)


def create_category_table(db):
    try:
        table_template = """ CREATE TABLE IF NOT EXISTS category (
                    id SERIAL PRIMARY KEY,
                    title text NOT NULL,
                    details text NOT NULL
        )
        """
        db.execute_query(table_template)
        print("Category table created.")
    except Exception as error:
        print(error)


def create_ticket_type_table(db):
    try:
        table_template = """ CREATE TABLE IF NOT EXISTS ticket_type (
                    id SERIAL PRIMARY KEY,
                    display_name text NOT NULL,
                    category_id INT REFERENCES category(id)
        )
        """
        db.execute_query(table_template)
        print("Ticket type table created.")
    except Exception as error:
        print(error)


def create_ticket_table(db):
    try:
        table_template = """ CREATE TABLE IF NOT EXISTS ticket (
                    id SERIAL PRIMARY KEY,
                    title text NOT NULL,
                    message text NOT NULL,
                    user_id INT REFERENCES users(id),
                    priority_id INT REFERENCES priority(id),
                    status_id INT REFERENCES status(id),
                    type_id INT REFERENCES ticket_type(id)
        )
        """
        db.execute_query(table_template)
        print("Ticket table created.")
    except Exception as error:
        print(error)


def create_ticket_logs_table(db):
    try:
        table_template = """ CREATE TABLE IF NOT EXISTS ticket_logs (
                    id SERIAL PRIMARY KEY,
                    content text NOT NULL,
                    ticket_id INT REFERENCES ticket(id)
        )
        """
        db.execute_query(table_template)
        print("Ticket logs table created.")
    except Exception as error:
        print(error)


def create_all_tables(db):
    try:
        create_user_table(db)
        create_priority_table(db)
        create_status_table(db)
        create_category_table(db)
        create_ticket_type_table(db)
        create_ticket_table(db)
        create_ticket_logs_table(db)
    except Exception as error:
        print(error)


def seed_priority(db):
    try:
        insert_query = """INSERT INTO priority (level) VALUES
                    ('High'),
                    ('Medium'),
                    ('Low')
        """
        db.execute_query(insert_query)
        print("Values inserted successfully. ✅")
    except Exception as error:
        print(error)


def seed_tables(db):
    try:
        seed_priority(db)
    except Exception as error:
        print(error)


if __name__ == "__main__":
    db = db_class.Database(CONFIG)
    drop_all_tables(db)
    create_all_tables(db)
    seed_tables(db)
