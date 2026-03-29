import pandas as pd
from datetime import timedelta

from market_data.loader import MarketDataLoader
from market_data.cache import MarketDataCache


class MarketData:
    def __init__(self, refresh_minutes: int = 10):
        self.loader = MarketDataLoader()
        self.cache = MarketDataCache()

        self.refresh_delta = timedelta(minutes=refresh_minutes)
        self._last_update = None
        self._loaded = False

    def load(self, start_date: pd.Timestamp, end_date: pd.Timestamp):
        df = self.loader.load(start_date, end_date)
        self.cache.load(df)

        self._last_update = pd.Timestamp.now()
        self._loaded = True

    def _is_stale(self) -> bool:
        if not self._loaded or self._last_update is None:
            return True

        return (pd.Timestamp.now() - self._last_update) > self.refresh_delta

    def ensure_loaded(self):
        if self._is_stale():
            today = pd.Timestamp("today").normalize()
            start = today - pd.DateOffset(days=5)

            self.load(start, today)

    def get(self, date, ticker, field):
        self.ensure_loaded()
        return self.cache.get(date, ticker, field)

    def get_series(self, ticker, field):
        self.ensure_loaded()
        return self.cache.get_series(ticker, field)

    def get_slice(self, date=None, ticker=None, field=None):
        self.ensure_loaded()
        return self.cache.get_slice(date, ticker, field)

    @property
    def last_update(self):
        return self._last_update