import streamlit as st

st.markdown("<h1>Review Authenticity Detection Dashboard</h1>", unsafe_allow_html=True)

# KPI Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        "<div class='card'><h2>Model</h2><h3>Transformer</h3></div>",
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        "<div class='card'><h2>XAI Module</h2><h3>Attention Explain</h3></div>",
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        "<div class='card'><h2>Platform</h2><h3>Streamlit Dashboard</h3></div>",
        unsafe_allow_html=True
    )

st.markdown("---")

st.subheader("Navigation")
st.info("Use sidebar to Predict Reviews, Explain Output and View Admin Logs.")
