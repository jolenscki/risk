import pandas as pd


class MarketDataCache:
    def __init__(self):
        self._df = None
        self._pivot = None

    def load(self, df: pd.DataFrame):
        self._df = df

        # Multi-index for fast lookup
        self._pivot = df.set_index(["date", "ticker", "field"])["value"].sort_index()

    def get(self, date, ticker, field):
        return self._pivot.loc[(pd.Timestamp(date), ticker, field)]

    def get_series(self, ticker, field):
        return self._pivot.xs((ticker, field), level=("ticker", "field"))

    def get_slice(self, date=None, ticker=None, field=None):
        idx = self._pivot

        if date is not None:
            idx = idx.xs(pd.Timestamp(date), level="date")

        if ticker is not None:
            idx = idx.xs(ticker, level="ticker")

        if field is not None:
            idx = idx.xs(field, level="field")

        return idx