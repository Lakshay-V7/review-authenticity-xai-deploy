import streamlit as st
import torch
import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import matplotlib.pyplot as plt

from model.config import MODEL_NAME

st.title(" Explain Review using Attention Heatmap")

review = st.text_area("Enter Review Text")

if st.button("Explain Review"):

    review = str(review).strip()

    if len(review) < 5:
        st.warning("Please enter valid review text")
        st.stop()

    st.success("Generating Attention Explanation...")

    # Load tokenizer + model with attentions ON
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

    model = AutoModelForSequenceClassification.from_pretrained(
        MODEL_NAME,
        output_attentions=True
    )

    # Tokenize input review
    inputs = tokenizer(
        review,
        return_tensors="pt",
        truncation=True,
        max_length=128,
        padding=True
    )

    #  Forward pass
    with torch.no_grad():
        outputs = model(**inputs)

    # ---------------------------------------------------
    #  Correct Attention Extraction
    # attentions shape = (batch, heads, seq_len, seq_len)
    # ---------------------------------------------------

    attentions = outputs.attentions[-1]  # last layer

    # Step 1: Average over all heads
    attn_avg = attentions.mean(dim=1)  # (batch, seq_len, seq_len)

    # Step 2: Token importance score = average attention received
    token_scores = attn_avg[0].mean(dim=0)  # (seq_len,)

    attention_scores = token_scores.numpy()

    # ✅ Tokens list
    tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])

    # ---------------------------------------------------
    # ✅ Plot Top Tokens
    # ---------------------------------------------------

    st.subheader("🔍 Important Words (Attention Scores)")

    # Limit tokens for clean display
    N = min(20, len(tokens))

    fig, ax = plt.subplots(figsize=(12, 4))
    ax.bar(tokens[:N], attention_scores[:N], color="orange")

    ax.set_title("Top Important Tokens (Attention)")
    ax.set_ylabel("Attention Weight")

    plt.xticks(rotation=45)
    st.pyplot(fig)

    # ---------------------------------------------------
    # ✅ Show Prediction Also
    # ---------------------------------------------------

    probs = torch.nn.functional.softmax(outputs.logits, dim=1).numpy()[0]

    st.subheader(" Model Prediction Probabilities")

    st.write(f"Class 0 Probability: {probs[0]:.4f}")
    st.write(f"Class 1 Probability: {probs[1]:.4f}")

    st.info("Higher attention words contribute more to the prediction.")
