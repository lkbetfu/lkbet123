import random
import pandas as pd
from datetime import datetime
import os

class MultiplierLogger:
    def __init__(self):
        self.data = []
        self.csv_path = "multiplier_log.csv"

    def simulate_next_multiplier(self):
        r = random.random()
        if r < 0.01:
            multiplier = random.choice([100, 500, 1000])
        else:
            multiplier = round(random.uniform(1, 50), 2)
        return multiplier

    def log_multiplier(self, multiplier):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data.append({"timestamp": now, "multiplier": multiplier})

    def get_dataframe(self):
        return pd.DataFrame(self.data)

    def save_to_csv(self, df):
        if not df.empty:
            df.to_csv(self.csv_path, index=False)
