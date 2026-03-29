from products.core.product import Product
import pandas as pd


class USDBRLFuture(Product):
    def __init__(self, maturity: pd.Timestamp):
        super().__init__(f"USDBRL_{maturity.date()}", "BZ", maturity)

    def get_PU(self, date: pd.Timestamp):
        return 5.0  # FX level placeholder

    def get_risk(self, date: pd.Timestamp, risk_factor: str, dy=0.01):
        return dy * 1000