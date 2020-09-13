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
    except Error as e:
        print(e)

    
def show_database(conn):

    c = conn.cursor()

    c.execute("""SELECT * FROM register""")
    print(c.fetchall())

def create_material(conn, material):
    sql =""" INSERT INTO materials(name, price) VALUES(?,?) """
    cur = conn.cursor()
    cur.execute(sql, material)
    conn.commit()
    
    return cur.lastrowid

def create_register(conn, register):
    sql =""" INSERT INTO register(name, value, date, time) VALUES(?,?,?,?) """

    cur = conn.cursor()
    cur.execute(sql, register)
    conn.commit()
    
    return cur.lastrowid

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
        value text NOT NULL,
        date text,
        time text
    );"""

    conn = create_connection(database)
    
    if conn is not None: 
        create_table(conn, sql_create_materials_table)
      
        create_table(conn, sql_create_register_table)

        show_database(conn)
    else: 
        print("Error! Cannot create the database connection.")

if __name__ == "__main__":
    main()