import sqlite3
from datetime import datetime

DB_PATH = "storage/codeagent.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_type TEXT,
                model_name TEXT,
                user_input TEXT,
                response TEXT,
                timestamp TEXT
            )
        """)
        conn.commit()

def log_interaction(task_type, model_name, user_input, response):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO history (task_type, model_name, user_input, response, timestamp)
            VALUES (?, ?, ?, ?, ?)
        """, (task_type, model_name, user_input, response, datetime.now().isoformat()))
        conn.commit()

def get_history(limit=10):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT task_type, model_name, user_input, response, timestamp
            FROM history
            ORDER BY id DESC LIMIT ?
        """, (limit,))
        return cursor.fetchall()
