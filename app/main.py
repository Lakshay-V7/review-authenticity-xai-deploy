import streamlit as st
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from streamlit_option_menu import option_menu
from app.auth import login

# Load CSS
with open("app/assets/style.css", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(page_title="Review Authenticity XAI", layout="wide")

st.title("Review Authenticity Detection Dashboard")

# LOGIN
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.subheader("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if login(username, password):
            st.session_state.authenticated = True
            st.session_state.user = username
            st.success("Login Successful ✅")
            st.rerun()
        else:
            st.error("Invalid Credentials ❌")

else:
    st.sidebar.success(f"Logged in as {st.session_state.user}")

    menu = option_menu(
        "Navigation",
        ["Predict", "Explain", "Admin Panel", "About"],
        icons=["search", "brain", "shield-lock", "info-circle"],
        menu_icon="cast",
        default_index=0,
    )

    if menu == "Predict":
        exec(open("app/pages/1_Predict.py", encoding="utf-8").read())

    elif menu == "Explain":
        exec(open("app/pages/2_Explain.py", encoding="utf-8").read())

    elif menu == "Admin Panel":
        exec(open("app/pages/3_Admin.py", encoding="utf-8").read())

    elif menu == "About":
        exec(open("app/pages/4_About.py", encoding="utf-8").read())
