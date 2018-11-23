import psycopg2
import psycopg2.extras
from werkzeug.security import generate_password_hash

url = "dbname='SendIT' host='localhost' port='5432' user='postgres' password='new1'"


class Users:
    # user object that defines all methods taken by users
    def __init__(self, user_name=None, email=None, password=None, role="user"):
        self.user_name = user_name
        self.email = email
        self.password = password
        self.role = role

    def signup(self):
        # the user creates an account and their details are saved in the database
        con = psycopg2.connect(url)
        cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "insert into users VALUES (DEFAULT,%s,%s,%s,%s)"
        cur.execute(query, (self.user_name, self.email, self.password, self.role))
        con.commit()
        con.close()

    def admin(self, is_admin='admin'):
        con = psycopg2.connect(url)
        cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "insert into users VALUES (DEFAULT,%s,%s,%s,%s)"
        cur.execute(query, (self.user_name, self.email, self.password, is_admin))
        con.commit()
        con.close()



    @staticmethod
    def find_by_username(username):
        # find user by username
        con = psycopg2.connect(url)
        cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * FROM users WHERE user_name=%s",(username,))
        user = cur.fetchone()
        if user:
            return user
        return {"message": "Not found"}

    def find_by_user_id(self, user_id):
        # find a user by userid
        con = psycopg2.connect(url)
        cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
        user = cur.fetchone()
        return user





