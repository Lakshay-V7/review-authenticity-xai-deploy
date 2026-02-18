import pandas as pd
from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer
)
import torch

# -----------------------------
# 1. Load Balanced Dataset
# -----------------------------
print("Loading balanced dataset...")

df = pd.read_csv("dataset/yelp_balanced.csv")

print(df.head())
print("Dataset Size:", len(df))

# Convert to HuggingFace Dataset
dataset = Dataset.from_pandas(df)

# Split into Train/Test
dataset = dataset.train_test_split(test_size=0.2)

train_data = dataset["train"]
test_data = dataset["test"]

# -----------------------------
# 2. Load Tokenizer + Model
# -----------------------------
MODEL_NAME = "distilbert-base-uncased"

print("Loading tokenizer + model...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

def tokenize_function(example):
    return tokenizer(
        example["text"],
        truncation=True,
        padding="max_length",
        max_length=128
    )

train_data = train_data.map(tokenize_function, batched=True)
test_data = test_data.map(tokenize_function, batched=True)

# Format dataset for PyTorch
train_data.set_format("torch", columns=["input_ids", "attention_mask", "target"])
test_data.set_format("torch", columns=["input_ids", "attention_mask", "target"])

model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_NAME,
    num_labels=2
)

# -----------------------------
# 3. Training Arguments
# -----------------------------
training_args = TrainingArguments(
    output_dir="model/fake_review_model",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=2,
    weight_decay=0.01,
    logging_dir="./logs",
    logging_steps=50
)

# -----------------------------
# 4. Trainer Setup
# -----------------------------
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_data,
    eval_dataset=test_data,
)

# -----------------------------
# 5. Train Model
# -----------------------------
print("🚀 Training Started...")
trainer.train()

# -----------------------------
# 6. Save Final Model
# -----------------------------
print("Saving model...")
trainer.save_model("model/fake_review_model")
tokenizer.save_pretrained("model/fake_review_model")

print(" Training Complete! Model saved in model/fake_review_model")
