import sqlite3

class DatabaseManager:
    def __init__(self, database_name):
        self.con = self.connect_database(database_name)
        self.cursor = self.con.cursor()

    def connect_database(self, database_name):
        con = sqlite3.connect(database_name)
        return con

    def fetch_tables(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = self.cursor.fetchall()
        return tables
    
    def select_slot_two(self,name):
        self.cursor.execute(f"PRAGMA table_info({name});")
        tables = self.cursor.fetchall()
        return tables
        

    def close_database(self):
        self.con.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close_database()
