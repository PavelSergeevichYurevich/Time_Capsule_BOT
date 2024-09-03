import sqlite3

class Connect():
    def __init__(self, name:str) -> None:
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()
        self.cursor.executescript('''
            CREATE TABLE IF NOT EXISTS Letters (
                   user_id INTEGER PRIMARY KEY,
                   telegram_id INTEGER,
                   fio TEXT NOT NULL,
                   letter TEXT NOT NULL,
                   date TEXT
            )
        ''')
        self.connection.commit()
                    
    def insert(self, telegram_id:int, fio:str, letter:str, date:str) -> None:
        self.cursor = self.connection.cursor()
        self.cursor.execute('INSERT INTO Letters (telegram_id, fio, letter, date) VALUES (?, ?, ?, ?)', (telegram_id, fio, letter, date))
        self.connection.commit()
    
    def __del__(self):
        self.connection.close()