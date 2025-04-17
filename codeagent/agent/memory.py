import sqlite3

def init_db():
    conn = sqlite3.connect("memory.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS memory (id INTEGER PRIMARY KEY, input TEXT, output TEXT)")
    conn.commit()
    conn.close()

def save_to_memory(user_input, output):
    conn = sqlite3.connect("memory.db")
    c = conn.cursor()
    c.execute("INSERT INTO memory (input, output) VALUES (?, ?)", (user_input, output))
    conn.commit()
    conn.close()
