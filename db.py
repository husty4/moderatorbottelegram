import sqlite3
import time

class database:
    def __init__(self):
        self.connection = sqlite3.connect(Database)
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'users' WHERE 'user_id' = ?,"(user_id,)).fetchall()
            return bool(len(result))

    def add_user(self, user_id):
        with self.connection:
            return self.connection.execute("INSERT INTO 'users' ('user_id') VALUES (?)", (user_id,))