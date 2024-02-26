import sqlite3

def connect_database(database_name):
    con = sqlite3.connect(database_name)
    return con

def fetch_tables(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    return tables

def close_database(con):
    con.close()