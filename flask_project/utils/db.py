import sqlite3

DB_NAME = "chat_history.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT,
            prompt TEXT,
            response TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_entry(role, prompt, response):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO history (role, prompt, response) VALUES (?, ?, ?)",
        (role, prompt, response)
    )
    conn.commit()
    conn.close()

def fetch_history():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT role, prompt, response FROM history ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()
    return rows

def clear_history_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM history")
    conn.commit()
    conn.close()