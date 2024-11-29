import sqlite3

def initialize_db():
    conn = sqlite3.connect('complaintDB.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS complaints
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       description TEXT,
                       status TEXT)''')
    conn.commit()
    conn.close()

initialize_db()
