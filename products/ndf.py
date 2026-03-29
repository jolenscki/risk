from products.core.product import Product
import pandas as pd


class NDF(Product):
    def __init__(self, ccy: str, maturity: pd.Timestamp):
        super().__init__(f"NDF_{ccy}_{maturity.date()}",
                         calendar=f"{ccy}+US",
                         maturity=maturity)
        self.ccy = ccy

    def get_PU(self, date: pd.Timestamp):
        return 1.0

    def get_risk(self, date: pd.Timestamp, risk_factor: str, dy=0.01):
        return dy * 500


class BRLNDF(NDF):
    def __init__(self, maturity: pd.Timestamp):
        super().__init__("BRL", maturity)


class COPNDF(NDF):
    def __init__(self, maturity: pd.Timestamp):
        super().__init__("COP", maturity)


class CLPNDF(NDF):
    def __init__(self, maturity: pd.Timestamp):
        super().__init__("CLP", maturity)