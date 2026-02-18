import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

st.title("🛡 Admin Analytics Panel")

LOG_FILE = "logs/reviews_log.csv"

# Safe file check
if not os.path.exists(LOG_FILE):
    st.warning("No reviews logged yet. Please predict some reviews first.")
    st.stop()

df = pd.read_csv(LOG_FILE)

# ----------------------------
# ✅ KPI Metrics
# ----------------------------
total = len(df)
fake = len(df[df["Prediction"] == "Fake Review"])
genuine = len(df[df["Prediction"] == "Genuine Review"])

col1, col2, col3 = st.columns(3)

col1.metric("Total Reviews", total)
col2.metric("Fake Reviews", fake)
col3.metric("Genuine Reviews", genuine)

st.markdown("---")

# ----------------------------
# ✅ Pie Chart
# ----------------------------
st.subheader("Fake vs Genuine Distribution")

fig, ax = plt.subplots()
ax.pie(
    [fake, genuine],
    labels=["Fake", "Genuine"],
    autopct="%1.1f%%",
    colors=["red", "green"]
)
st.pyplot(fig)

st.markdown("---")

# ----------------------------
# ✅ Logs Table
# ----------------------------
st.subheader(" Review History")
st.dataframe(df.tail(20), use_container_width=True)

# ----------------------------
# ✅ Download Logs Button
# ----------------------------
st.download_button(
    label=" Download Full Log CSV",
    data=df.to_csv(index=False),
    file_name="reviews_log.csv",
    mime="text/csv"
)
