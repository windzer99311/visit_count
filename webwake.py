import streamlit as st
import sqlite3

DB_FILE = "counter.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS counter (
            id INTEGER PRIMARY KEY,
            visits INTEGER
        )
    ''')
    # Initialize with 0 if empty
    c.execute('SELECT COUNT(*) FROM counter')
    if c.fetchone()[0] == 0:
        c.execute('INSERT INTO counter (id, visits) VALUES (1, 0)')
    conn.commit()
    conn.close()

def increment_counter():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('UPDATE counter SET visits = visits + 1 WHERE id = 1')
    conn.commit()
    c.execute('SELECT visits FROM counter WHERE id = 1')
    visits = c.fetchone()[0]
    conn.close()
    return visits

# --- Main Streamlit App ---
st.set_page_config(page_title="Visitor Counter", layout="centered")
st.title("👋 Welcome to the Site")

init_db()
count = increment_counter()

st.success(f"👀 Visitors: {count}")
