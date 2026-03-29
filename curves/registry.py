import pandas as pd
from curves.di import DICurve


class CurveRegistry:
    _cache = {}

    @classmethod
    def get(cls, name: str, ref_date):
        key = (name, pd.Timestamp(ref_date))

        if key not in cls._cache:
            if name == "DI":
                curve = DICurve().build(ref_date)
            else:
                raise ValueError(f"Unknown curve {name}")

            cls._cache[key] = curve

        return cls._cache[key]