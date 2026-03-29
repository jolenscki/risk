from products.core.product import Product
import pandas as pd


class Swap(Product):
    def __init__(self, name: str, calendar: str, maturity: pd.Timestamp):
        super().__init__(name, calendar, maturity)

    def get_PU(self, date: pd.Timestamp):
        return 100.0

    def get_risk(self, date: pd.Timestamp, risk_factor: str, dy=0.01):
        return dy * 10000


class PRECDIOffshore(Swap):
    def __init__(self, maturity: pd.Timestamp):
        super().__init__("PRE_CDI_OFF", "BZ+US", maturity)


class SOFROIS(Swap):
    def __init__(self, maturity: pd.Timestamp):
        super().__init__("SOFR_OIS", "US", maturity)


class COPSwap(Swap):
    def __init__(self, maturity: pd.Timestamp):
        super().__init__("COP_SWAP", "CO", maturity)


class CLPSwap(Swap):
    def __init__(self, maturity: pd.Timestamp):
        super().__init__("CLP_SWAP", "CL", maturity)


class MXNOIS(Swap):
    def __init__(self, maturity: pd.Timestamp):
        super().__init__("MXN_OIS_TIIE", "MX", maturity)