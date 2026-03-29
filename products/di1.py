import pandas as pd
from products.core.product import Product


class DI1Future(Product):
    def __init__(self, maturity: pd.Timestamp):
        super().__init__(name=f"DI1_{maturity.date()}",
                         calendar="BZ",
                         maturity=maturity)

    def get_PU(self, date: pd.Timestamp):
        # placeholder
        return 100000 / (1 + 0.10)

    def get_risk(self, date: pd.Timestamp, risk_factor: str, dy: float = 0.01):
        base = self.get_PU(date)
        shocked = base * (1 + dy)
        return shocked - base
    