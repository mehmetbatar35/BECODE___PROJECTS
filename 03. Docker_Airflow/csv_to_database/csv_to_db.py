import sqlite3
import os

db_path = os.path.join('db', 'football_prediction.db')

if not os.path.exists('db'):
    os.mkdir('db')

conn = sqlite3.connect(db_path)

conn.close()
print(f"Database saved to {db_path}")












