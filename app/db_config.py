import psycopg2
import psycopg2.extras
import os
from instance.config import app_config

env = os.getenv("FLASK_ENV")

url = app_config[env].DATABASE_URI

def create_connection(url):
   con = psycopg2.connect(url)
   return con

def init_db():
    con = create_connection(url)
    return con
def create_tables():
    new_connection = init_db()
    cur = new_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    tables = ('''CREATE TABLE IF NOT EXISTS users(
                        user_id serial PRIMARY KEY ,
                        user_name VARCHAR  (80) NOT NULL,
                        email VARCHAR (80) NOT NULL ,
                        password VARCHAR (200) NOT NULL,
                        role VARCHAR (50) NOT NULL
                        );''',
              '''CREATE TABLE IF NOT EXISTS orders(
                        order_id serial PRIMARY KEY ,
                        user_id integer REFERENCES users(user_id) ON DELETE CASCADE,
                        sender_name VARCHAR (20) NOT NULL,
                        phone_number VARCHAR (14) NOT NULL ,
                        id_number INTEGER NOT NULL,
                        location VARCHAR (20) NOT NULL,
                        address VARCHAR (20) NOT NULL ,
                        weight INTEGER NOT NULL ,
                        destination VARCHAR (50) NOT NULL ,
                        price INTEGER NOT NULL,
                        status VARCHAR (50) NOT NULL DEFAULT 'undelivered'
                        );''')
    for item in tables:
        cur.execute(item)
        new_connection.commit()

    # cur.execute(tables)
    # new_connection.commit()

def drop_tables():
    drop = init_db()
    cur = drop.cursor()
    query = (
        """DROP TABLE IF EXISTS orders CASCADE""", """DROP TABLE IF EXISTS users CASCADE ;""",
    )
    for item in query:
        cur.execute(item)
        drop.commit()



