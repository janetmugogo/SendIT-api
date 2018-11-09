import psycopg2

url = "dbname='SendIT' host='localhost' user='root' port='5263'  password='password'"


def connection(url):
    con = psycopg2.connect(url)
    return con


def init_db():
    con = connection(url)
    return con


# insert sql commands here,describe table and entities
def create_tables():
    cursor.execute(sql)

    # disconnect from server
    db.close()

    conn = connection(url)
    cursor = conn.cursor()
    queries = tables()
    for query in queries:
        cursor.execute(query)
    conn.commit()


def destroy_tables():
    pass


# tinsert tables query=[table1,table2] return query
def tables():
    table1 = """CREATE TABLE IF NOT EXISTS  ORDER(
                      order_id serial PRIMARYKEY NOT NULL, name CHAR(20) NOT NULL,
                       phonenumber INT, idnumber INT, 
                       location CHAR(20), 
                       address CHAR, weight INT)"""
    q = [table1]
    return query
