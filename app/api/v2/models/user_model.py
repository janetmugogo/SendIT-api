import psycopg2
import psycopg2.extras
from werkzeug.security import generate_password_hash, check_password_hash

# from app.db_config import url
url = "dbname='SendIT' host='localhost' port='5432' user='postgres' password='new1'"

class Users():
    #user object that defines all methods taken by users
    def __init__(self, user_name=None, email=None, password=None, role="user"):
        self.user_name = user_name
        self.email = email
        self.password = password
        self.role = role

    # the user creates an account and their details are saved
    def signup(self):
        con = psycopg2.connect(url)
        cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "insert into users VALUES (DEFAULT,%s,%s,%s,%s)"
        cur.execute(query, (self.user_name, self.email, self.password, self.role))
        con.commit()
        con.close()
    #find user by username
    def find_by_username(self, username):
        con = psycopg2.connect(url)
        cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * FROM users WHERE user_name = %s", (username,))
        user = cur.fetchone()
        # print(user)
        # # user = cur.fetchall()
        # if user:
        return user






