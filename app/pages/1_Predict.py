import streamlit as st
from model.detector import predict_review
from utils.logger import save_review

st.title(" Fake Review Prediction")

review = st.text_area("Enter Review Text:")

if st.button("Detect Authenticity"):

    if review.strip() == "":
        st.warning(" Please enter some review text.")
    else:
        #  Prediction
        label, score = predict_review(review)

        st.markdown("---")
        st.subheader(" Prediction Result")

        # ✅ Professional Output
        if label == "Fake Review":
            st.error(" Fake Review Detected!")
        else:
            st.success("✅ Genuine Review Detected!")

        st.info(f"Confidence Score: **{score:.2f}**")

        # Progress bar
        st.progress(int(score * 100))

        #  Save review log
        save_review(review, label, score)

        st.toast("Review saved successfully!")
