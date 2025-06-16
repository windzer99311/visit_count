import streamlit as st
import socket
import os

VISITOR_FILE = "visitors.txt"

def get_ip():
    """Try to get the visitor's IP address."""
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        return ip
    except:
        return "unknown"

def load_visitors():
    """Load visitor IPs from the file."""
    if not os.path.exists(VISITOR_FILE):
        return set()
    with open(VISITOR_FILE, "r") as file:
        return set(file.read().splitlines())

def save_visitor(ip):
    """Save a new visitor IP."""
    with open(VISITOR_FILE, "a") as file:
        file.write(ip + "\n")

# --- Main App ---
st.set_page_config(page_title="Visitor Counter", layout="centered")

st.title("🌐 Visitor Counter Web App")

ip = get_ip()
visitors = load_visitors()

if ip not in visitors:
    save_visitor(ip)
    visitors.add(ip)

st.success(f"🎉 Unique Visitors: {len(visitors)}")
st.write(f"Your IP: `{ip}`")
