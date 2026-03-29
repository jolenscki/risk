import numpy as np
from scipy.interpolate import interp1d


def get_interpolator(x, y, method="linear"):
    x = np.asarray(x)
    y = np.asarray(y)

    if method == "linear":
        return interp1d(x, y, kind="linear", fill_value="extrapolate")

    if method == "loglinear":
        return lambda t: np.exp(
            interp1d(x, np.log(y), kind="linear", fill_value="extrapolate")(t)
        )

    if method == "exponential":
        return lambda t: np.exp(
            interp1d(x, np.log(y), kind="linear", fill_value="extrapolate")(t)
        )

    raise ValueError(f"Unknown interpolation: {method}")