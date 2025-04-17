import sqlite3

DB_PATH = "storage/codeagent.db"

def init_memory():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS memory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                label TEXT,
                content TEXT
            )
        """)
        conn.commit()

def add_memory(label, content):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO memory (label, content) VALUES (?, ?)", (label, content))
        conn.commit()

def search_memory(keyword):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT label, content FROM memory WHERE content LIKE ?", (f"%{keyword}%",))
        return cursor.fetchall()
