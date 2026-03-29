from abc import ABC, abstractmethod
import pandas as pd


class Product(ABC):
    def __init__(self, name: str, calendar: str, maturity: pd.Timestamp):
        self._name = name
        self._calendar = calendar
        self._maturity = maturity

    def __repr__(self):
        return self._name

    def get_name(self) -> str:
        return self._name

    def get_calendar(self) -> str:
        return self._calendar

    def get_maturity(self) -> pd.Timestamp:
        return self._maturity

    @abstractmethod
    def get_PU(self, date: pd.Timestamp):
        pass

    @abstractmethod
    def get_risk(self, date: pd.Timestamp, risk_factor: str, dy: float = 0.01):
        pass
    