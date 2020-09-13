import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        print(c.fetchall())
    except Error as e:
        print(e)

def show_database():
    pass
def main():
    database = "database.db"

    sql_create_materials_table = """ CREATE TABLE IF NOT EXISTS materials (
    id integer PRIMARY KEY,
    name text NOT NULL,
    price integer NOT NULL
    );"""

    sql_create_register_table = """ CREATE TABLE IF NOT EXISTS register (
        id integer PRIMARY KEY, 
        name text NOT NULL, 
        value integer NOT NULL
    );"""

    conn = create_connection(database)
    
    if conn is not None: 
        create_table(conn, sql_create_materials_table)
      
        create_table(conn, sql_create_register_table)
    else: 
        print("Error! Cannot create the database connection.")

if __name__ == "__main__":
    main()