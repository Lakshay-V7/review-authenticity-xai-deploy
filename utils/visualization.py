import streamlit as st

def show_highlighted_tokens(tokens):
    """
    Display important tokens in a clean highlighted format.
    """
    st.subheader("Important Words Highlighted:")

    for word, score in tokens:
        st.markdown(f" **{word}** → Importance: `{score:.4f}`")
