import pandas as pd
from market_data import get_slice
from curves.core import Curve
from curves.spec import CurveSpec
from calendar import get_calendar


class CurveBuilder:
    def __init__(self, spec: CurveSpec):
        self.spec = spec

    def build(self, ref_date: pd.Timestamp):

        data = get_slice(date=ref_date).unstack("field")
        calendar = get_calendar(self.spec.calendar) if self.spec.calendar else None
        nodes = []

        for ticker, row in data.iterrows():
            if not self.spec.tickers_filter(ticker):
                continue

            if pd.isna(row.get("PX_LAST")):
                continue

            x = self.spec.x_transform(row, ticker, ref_date, calendar)
            y = self.spec.value_transform(row, ticker, ref_date)

            nodes.append((x, y))

        df = pd.DataFrame(nodes, columns=["x", "y"]).sort_values("x")

        return Curve(
            name=self.spec.name,
            crv=df,
            daycount=self.spec.daycount,
            calendar=self.spec.calendar,
            interp=self.spec.interp,
            ref_date=ref_date,
        )