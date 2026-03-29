from typing import Callable


class CurveSpec:
    def __init__(
        self,
        name: str,
        tickers_filter: Callable,
        x_transform: Callable,  
        maturity_parser: Callable,
        value_transform: Callable,
        daycount: str,
        calendar: str | None,
        interp: str = "linear",
    ):
        """
        tickers_filter: function(ticker: str) -> bool
        maturity_parser: function(ticker: str, ref_date) -> pd.Timestamp
        value_transform: function(price: float, ticker: str, ref_date) -> float
        x_transform: (row, ticker, ref_date, calendar) -> float
        """
        self.name = name
        self.tickers_filter = tickers_filter
        self.x_transform = x_transform
        self.maturity_parser = maturity_parser
        self.value_transform = value_transform
        self.daycount = daycount
        self.calendar = calendar
        self.interp = interp
        