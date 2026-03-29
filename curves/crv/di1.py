import pandas as pd
from curves.spec import CurveSpec
from curves.builder import CurveBuilder


# -------------------------
# DI-specific logic
# -------------------------

def di_filter(ticker: str) -> bool:
    return ticker.startswith("OD") and ticker.endswith("Comdty")


def di_maturity_parser(row, ticker: str, ref_date: pd.Timestamp) -> pd.Timestamp:
    """
    Use Bloomberg field directly
    """
    return pd.Timestamp(row["DT_FUT_LAST_DLV"])


def di_x_transform(row, ticker, ref_date, calendar):
    maturity = pd.Timestamp(row["DT_FUT_LAST_DLV"])

    # BUS252 year fraction
    return calendar.bday_count(ref_date, maturity) / 252.0


def di_value_transform(row, ticker, ref_date):
    return row["PX_LAST"] / 100.0


# -------------------------
# Spec
# -------------------------

DI_SPEC = CurveSpec(
    name="DI",
    tickers_filter=di_filter,
    maturity_parser=di_maturity_parser,
    value_transform=di_value_transform,
    daycount="BUS252",
    calendar="BZ",
    interp="exponential",
)


# -------------------------
# Builder interface
# -------------------------

class DICurve:
    def __init__(self):
        self.builder = CurveBuilder(DI_SPEC)

    def build(self, ref_date: pd.Timestamp):
        return self.builder.build(ref_date)