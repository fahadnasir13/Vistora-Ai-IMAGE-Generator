import streamlit as st
import os
from utils.auth import login_user, register_user, get_user, logout_user
from utils.credits import check_credits, deduct_credit
from utils.emailer import send_email
from utils.admin import admin_panel
from utils.generator import generate_image
import json
from utils.emailer import send_email
 
st.set_page_config(page_title="AI Image Generator", layout="wide")

if "user" not in st.session_state:
    st.session_state.user = None

st.title("🎨 AI Image Generator with Login & Credits")

if st.session_state.user:
    st.sidebar.success(f"Logged in as {st.session_state.user}")
    if st.button("Logout" ):
        logout_user()
        st.experimental_rerun()

    is_admin = st.session_state.user == "admin"
    if is_admin:
        admin_panel()

    with st.form("gen_form"):
        prompt = st.text_input("Enter prompt")
        submit = st.form_submit_button("Generate Image")

        if submit:
            if not check_credits():
                st.error("Not enough credits!")
            else:
                filename = generate_image(prompt, st.session_state.user)
                st.image(filename, caption="Generated Image")
                deduct_credit()
                send_email(st.session_state.user, prompt, filename)
else:
    st.subheader("Login or Register")
    with st.form("auth"):
        tab = st.radio("Choose", ["Login", "Register"])
        user = st.text_input("Username")
        pwd = st.text_input("Password", type="password")
        submit = st.form_submit_button("Submit")

        if submit:
            if tab == "Login":
                if login_user(user, pwd):
                    st.rerun()
                else:
                    st.error("Login failed")
            else:
                if register_user(user, pwd):
                    st.success("Registered! Please login")
                else:
                    st.error("User already exists")