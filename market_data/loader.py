from cupom.handler.resources import ResourcesHandler
import pandas as pd


class MarketDataLoader:
    def __init__(self):
        self.resources_handler = ResourcesHandler()

    def load(self, start_date: pd.Timestamp, end_date: pd.Timestamp) -> pd.DataFrame:
        df = self.resources_handler.snowflake_handler.get(
            "bbg_data",
            start_date=start_date,
            end_date=end_date
        )

        # Standardize
        df["date"] = pd.to_datetime(df["date"]).dt.normalize()

        return df
    