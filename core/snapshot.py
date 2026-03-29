import time
import hashlib


class MarketDataSnapshot:
    def __init__(self, asof, last_update_ts):
        self.asof = asof
        self.last_update_ts = last_update_ts

        self.id = self._compute_id()

    def _compute_id(self):
        raw = f"{self.asof}-{self.last_update_ts}"
        return hashlib.md5(raw.encode()).hexdigest()

    def __repr__(self):
        return f"<Snapshot {self.id[:8]} asof={self.asof}>"