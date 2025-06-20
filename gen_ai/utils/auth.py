import json, bcrypt
from pathlib import Path

USERS_FILE = Path("data/users.json")

def load_users():
    if not USERS_FILE.exists(): USERS_FILE.write_text("{}")
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)

def register_user(username, password):
    users = load_users()
    if username in users:
        return False
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    users[username] = {"password": hashed, "credits": 5}
    save_users(users)
    return True

def login_user(username, password):
    users = load_users()
    user = users.get(username)
    if user and bcrypt.checkpw(password.encode(), user["password"].encode()):
        import streamlit as st
        st.session_state.user = username
        return True
    return False

def get_user():
    import streamlit as st
    return st.session_state.get("user")

def logout_user():
    import streamlit as st
    st.session_state.user = None