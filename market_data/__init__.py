from market_data.core import MarketData

# default instance
_mkt = MarketData()


def configure(refresh_minutes: int = 10):
    global _mkt
    _mkt = MarketData(refresh_minutes=refresh_minutes)


def load(start_date, end_date):
    _mkt.load(start_date, end_date)


def get(date, ticker, field):
    return _mkt.get(date, ticker, field)


def get_series(ticker, field):
    return _mkt.get_series(ticker, field)


def get_slice(date=None, ticker=None, field=None):
    return _mkt.get_slice(date, ticker, field)


def last_update():
    return _mkt.last_update


__all__ = [
    "configure",
    "load",
    "get",
    "get_series",
    "get_slice",
    "last_update",
]
