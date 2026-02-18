from transformers import pipeline
from model.config import MODEL_NAME

# Load your trained model
classifier = pipeline(
    "text-classification",
    model=MODEL_NAME,
    tokenizer=MODEL_NAME
)

def predict_review(text):
    result = classifier(text)[0]

    label = result["label"]
    score = result["score"]

    # LABEL_0 = Fake, LABEL_1 = Genuine
    if label == "LABEL_0":
        return "Fake Review", score
    else:
        return "Genuine Review", score
