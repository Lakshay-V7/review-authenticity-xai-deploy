import os
import pandas as pd
from datetime import datetime

LOG_FILE = "logs/reviews_log.csv"

def save_review(review, label, score):

    #  Ensure logs folder exists
    os.makedirs("logs", exist_ok=True)

    new_data = {
        "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Review": review,
        "Prediction": label,
        "Score": round(score, 4)
    }

    #  Create file if not exists
    if not os.path.exists(LOG_FILE):
        df = pd.DataFrame([new_data])
        df.to_csv(LOG_FILE, index=False)

    else:
        df = pd.read_csv(LOG_FILE)
        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
        df.to_csv(LOG_FILE, index=False)
