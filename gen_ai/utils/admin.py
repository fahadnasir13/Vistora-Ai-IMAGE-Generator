from .credits import refill_credits
import streamlit as st

def admin_panel():
    st.sidebar.header("Admin Tools")
    user = st.sidebar.text_input("User to refill")
    amt = st.sidebar.number_input("Credits", 1, 100, step=1)
    if st.sidebar.button("Refill"):
        refill_credits(user, amt)
        st.sidebar.success(f"Refilled {amt} credits to {user}")
