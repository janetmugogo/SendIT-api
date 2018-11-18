import psycopg2
import os

DB_HOST = 'localhost'
DB_USERNAME = 'postgres'
DB_PASS = 'root'
DB_NAME = 'SendIT'
DB_PORT = 5432

url = "dbname='SendIT' host='localhost' port='5432' user='postgres' password='new1'"

db_url = os.getenv('DATABSE_URL')

# creating database connection
con = psycopg2.connect(url)


#creating the cursor
cur = con.cursor()

table1 = '''CREATE TABLE IF NOT EXISTS users(
                    user_id serial PRIMARY KEY ,
                    user_name VARCHAR  (80) NOT NULL,
                    email VARCHAR (80) NOT NULL ,
                    password VARCHAR (80) NOT NULL,
                    role VARCHAR (50) NOT NULL
                    );'''

table2 = '''CREATE TABLE IF NOT EXISTS orders(
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
                    );'''
cur.execute(table1, table2 )
con.commit()
