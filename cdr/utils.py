import pandas as pd


def get_days(start, end):
    return (pd.Timestamp(end) - pd.Timestamp(start)).days


def get_bdays(start, end, cal):
    return cal.bday_count(start, end)


def get_adj_bday(date, cal, convention):
    return cal.adjust(pd.Series([date]), convention).iloc[0]