# +
# stream/api_stream.py

import time
import pandas as pd
from stream.base_stream import BaseStream

class APIPollingStream(BaseStream):
    def __init__(self, fetch_fn, polling_interval=60):
        """
        Args:
            fetch_fn: A user-defined function that returns a pandas DataFrame with new rows
            polling_interval: Seconds between polls
        """
        self.fetch_fn = fetch_fn
        self.polling_interval = polling_interval
        self.seen = set()

    def stream(self):
        while True:
            df = self.fetch_fn()
            for _, row in df.iterrows():
                ts = row.name if row.name not in self.seen else None
                if ts and ts not in self.seen:
                    self.seen.add(ts)
                    yield row
            time.sleep(self.polling_interval)

