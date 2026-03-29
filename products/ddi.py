from products.core.product import Product
import pandas as pd


class DDIFuture(Product):
    def __init__(self, maturity: pd.Timestamp):
        super().__init__(f"DDI_{maturity.date()}", "BZ+US", maturity)

    def get_PU(self, date: pd.Timestamp):
        return 100000

    def get_risk(self, date: pd.Timestamp, risk_factor: str, dy=0.01):
        return 10.0
    