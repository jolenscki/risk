from market_data import MARKET_DATA
from curves.curve_manager import CurveManager


class PricingContext:

    def __init__(self, ref_date):
        self.ref_date = ref_date

        # snapshot locks everything
        self.snapshot = MARKET_DATA.get_snapshot(ref_date)

        self._curves = {}

    def get_curve(self, name):
        if name not in self._curves:
            self._curves[name] = CurveManager.get_curve(
                curve_name=name,
                ref_date=self.ref_date,
                snapshot=self.snapshot
            )

        return self._curves[name]

    @property
    def snapshot_id(self):
        return self.snapshot.id