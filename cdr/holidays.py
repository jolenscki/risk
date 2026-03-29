import pandas as pd
import holidays


MAP = {
        "BZ": holidays.Brazil,
        "US": holidays.UnitedStates,
        "CO": holidays.Colombia,
        "CL": holidays.Chile,
        "MX": holidays.Mexico,
        "SA": holidays.SouthAfrica,
        "SW": holidays.Sweden,
        "NO": holidays.Norway,
    }

def get_holidays(country_code: str, years: list[int]) -> pd.DatetimeIndex:
    """
    country_code mapping:
    BZ -> Brazil
    US -> UnitedStates
    CO -> Colombia
    CL -> Chile
    MX -> Mexico
    SA -> SouthAfrica
    SW -> Sweden
    NO -> Norway
    """

    if country_code not in MAP:
        raise ValueError(f"Unsupported country: {country_code}")

    hol = MAP[country_code](years=years)

    return pd.to_datetime(list(hol.keys())).normalize()
