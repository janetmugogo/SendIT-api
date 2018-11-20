from app.db_config import drop_tables, create_tables

if __name__ == '__main__':
    drop_tables()
    create_tables()