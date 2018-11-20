import psycopg2
import psycopg2.extras
import os

url = "dbname='SendIT' host='localhost' port='5432' user='postgres' password='new1'"

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
                        sender_name CHAR (20) NOT NULL,
                        phone_number VARCHAR (14) NULL ,
                        id_number INT  NULL,
                        location CHAR (20) NOT NULL,
                        address VARCHAR (20) NOT NULL ,
                        weight INT NOT NULL ,
                        status CHAR (50) NOT NULL ,
                        destination CHAR (50) NOT NULL ,
                        price INT NOT NULL
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



