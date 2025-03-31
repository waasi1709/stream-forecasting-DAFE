# +
# stream/simulated_stream.py

import time
import pandas as pd
from stream.base_stream import BaseStream

class SimulatedStream(BaseStream):
    def __init__(self, df: pd.DataFrame, delay: float = 0.0):
        self.df = df
        self.delay = delay

    def stream(self):
        for _, row in self.df.iterrows():
            yield row  # row is a pandas Series (row of features)
            if self.delay > 0:
                time.sleep(self.delay)

