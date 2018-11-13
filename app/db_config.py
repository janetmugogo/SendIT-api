# import psycopg2
#
# url = "dbname='SendIT' host='localhost' user='root' port='5432'  password='password'"
#
#
# def connection(url):
#     con = psycopg2.connect(url)
#     return con
#
#
# def init_db():
#     con = connection(url)
#     return con
#
#
# def create_tables():
#     conn = connection(url)
#     cursor = conn.cursor()
#     queries = tables()
#     for query in queries:
#         cursor.execute(query)
#     conn.commit()
#
#
# def destroy_tables():
#     pass
#
#
# # insert sql commands here,describe table and entities
# def tables():
#     table1 = """CREATE TABLE IF NOT EXISTS  ORDER(
#                       order_id serial PRIMARYKEY NOT NULL, name CHAR(20) NOT NULL,
#                        phonenumber INT, idnumber INT,
#                        location CHAR(20),
#                        address CHAR, weight INT)"""
#     table2 = """CREATE TABLE IF NOT EXISTS  USER(
#                           user_id serial PRIMARYKEY NOT NULL,
#                            username VARCHAR(50),  email VARCHAR(50),
#                            password VARCHAR(50) ,confirm_password VARCHAR(50)
#                            )"""
#     # insert tables query=[table1,table2] return query
#     query = [table1, table2]
#     return query
