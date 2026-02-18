import shap
from transformers import pipeline
from model.config import MODEL_NAME

classifier = pipeline("text-classification", model=MODEL_NAME)

explainer = shap.Explainer(classifier)

def explain_review(text):
    return explainer([text])
