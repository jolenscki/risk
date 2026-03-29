import pandas as pd
import numpy as np

from curves.interp import get_interpolator

class Curve:
    def __init__(
        self,
        name: str,
        crv: pd.DataFrame,
        daycount: str,
        calendar: str | None = None,
        interp: str = "linear",
        ref_date=None,
    ):
        self.name = name
        self.daycount = daycount
        self.calendar = calendar
        self.interp_type = interp
        self.ref_date = ref_date

        self.crv = crv.sort_values("x").copy()

        self._interp = get_interpolator(
            self.crv["x"].values,
            self.crv["y"].values,
            method=self.interp_type
        )

    def __call__(self, x):
        return self._interp(x)