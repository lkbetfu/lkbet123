import random
import pandas as pd
from datetime import datetime

class MultiplierLogger:
    def __init__(self):
        self.data = []

    def simulate_next_multiplier(self):
        # Simulate multiplier, rare high multipliers included randomly
        r = random.random()
        if r < 0.01:
            multiplier = random.choice([100, 500, 1000])
        else:
            multiplier = round(random.uniform(1, 50), 2)
        return multiplier

    def log_multiplier(self, multiplier):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data.append({"timestamp": now, "multiplier": multiplier})

    def get_high_multipliers(self):
        df = pd.DataFrame(self.data)
        if df.empty:
            return df
        return df[df["multiplier"] >= 100]