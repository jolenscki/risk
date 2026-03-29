import pandas as pd
from pandas.tseries.offsets import CustomBusinessDay
from cdr.holidays import get_holidays


class Calendar:
    def __init__(self, name: str, years=None, holidays=None):
        self.name = name

        if holidays is not None:
            self.holidays = pd.to_datetime(holidays).normalize()

        else:
            if years is None:
                years = list(range(1990, 2050))  # safe coverage

            if "+" in name:
                parts = sorted(name.split("+"))
                all_holidays = pd.DatetimeIndex([])

                for p in parts:
                    h = get_holidays(p, years)
                    all_holidays = all_holidays.union(h)

                self.holidays = all_holidays

            else:
                self.holidays = get_holidays(name, years)

        self._cbd = CustomBusinessDay(holidays=self.holidays)

    def __repr__(self):
        return self.name

    @property
    def cbd(self):
        return self._cbd

    def is_business_day(self, dates):
        dates = pd.to_datetime(dates)
        return dates == (dates + 0 * self._cbd)

    def adjust(self, dates, convention):
        from cdr.enums import RollConv

        dates = pd.to_datetime(dates)

        if convention == RollConv.UNADJUSTED:
            return dates

        if convention == RollConv.FOLLOWING:
            return dates + 0 * self._cbd

        if convention == RollConv.PRECEDING:
            return dates - 0 * self._cbd

        if convention == RollConv.MODIFIED_FOLLOWING:
            adj = dates + 0 * self._cbd
            mask = adj.dt.month != dates.dt.month
            adj[mask] = dates[mask] - 0 * self._cbd
            return adj

        if convention == RollConv.MODIFIED_PRECEDING:
            adj = dates - 0 * self._cbd
            mask = adj.dt.month != dates.dt.month
            adj[mask] = dates[mask] + 0 * self._cbd
            return adj

        raise ValueError(f"Unsupported convention: {convention}")

    def bday_range(self, start, end):
        return pd.date_range(start=start, end=end, freq=self._cbd)

    def bday_count(self, start, end):
        return len(self.bday_range(start, end)) - 1
    

class CalendarRegistry:
    _cache = {}
    _holiday_cache = {}

    @classmethod
    def get(cls, name: str):
        key = cls._normalize(name)

        if key not in cls._cache:
            holidays = cls._get_holidays(key)
            cls._cache[key] = Calendar(key, holidays=holidays)

        return cls._cache[key]

    @classmethod
    def _get_holidays(cls, name: str):
        if name in cls._holiday_cache:
            return cls._holiday_cache[name]

        # Compute once and cache
        cal = Calendar(name)
        cls._holiday_cache[name] = cal.holidays
        return cal.holidays

    @staticmethod
    def _normalize(name: str) -> str:
        if "+" in name:
            parts = sorted(name.split("+"))
            return "+".join(parts)
        return name
    