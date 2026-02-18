from transformers import AutoModelForSequenceClassification

path = "./model/fake_review_model"

model = AutoModelForSequenceClassification.from_pretrained(path)

model.config.id2label = {0: "LABEL_0", 1: "LABEL_1"}
model.config.label2id = {"LABEL_0": 0, "LABEL_1": 1}

model.save_pretrained(path)

print("✅ Labels Reset Done!")
