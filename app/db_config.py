import psycopg2

url = "dbname='SendIT' user='postgres' host='localhost' " + \
      "password='password'"


def connection(url):
    con = psycopg2.connect(url)
    return con


def init_db():
    con = connection(url)
    return con

 #insert sql commands here,describe table and entities
def create_tables():
    conn = connection(url)
    cursor = conn.cursor()
    queries = tables()
    for query in queries:
        cursor.execute(query)
    conn.commit()


def destroy_tables():
    pass

#tinsert tables query=[table1,table2] return query
def tables():
    pass