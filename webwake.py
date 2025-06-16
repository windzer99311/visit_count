import streamlit as st
import sqlite3
import socket
from datetime import datetime

DB_FILE = "visitors.db"

# Initialize DB
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS visitors (
            ip TEXT PRIMARY KEY,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Get user IP
def get_ip():
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        return ip
    except:
        return "unknown"

# Save visitor if new
def save_visitor(ip):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT ip FROM visitors WHERE ip=?', (ip,))
    if c.fetchone() is None:
        c.execute('INSERT INTO visitors (ip, timestamp) VALUES (?, ?)', (ip, datetime.now().isoformat()))
    conn.commit()
    conn.close()

# Get total unique visitors
def get_visitor_count():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM visitors')
    count = c.fetchone()[0]
    conn.close()
    return count

# Main App Logic
st.set_page_config(page_title="Persistent Visitor Counter")
st.title("🌐 Persistent Visitor Counter")

init_db()
ip = get_ip()
save_visitor(ip)
count = get_visitor_count()

st.success(f"🎉 Total Unique Visitors: {count}")
st.write(f"Your IP: `{ip}`")
