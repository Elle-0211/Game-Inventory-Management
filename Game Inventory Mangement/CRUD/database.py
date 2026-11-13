import mysql.connector
from mysql.connector import Error

class DatabaseManager:
    def __init__(self, user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                database=self.database
            )
            if self.connection.is_connected():
                print("Connected to the database")
                return True
        except Error as e:
            print(f"Error connecting to the database: {e}")
            return False

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")

    def execute_query(self, query, params=None, fetch=True):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        if fetch:
            result = cursor.fetchall()
            return result
        else:
            self.connection.commit()
            return None