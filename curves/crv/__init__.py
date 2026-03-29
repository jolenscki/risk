from curves.registry import CurveRegistry


def get_curve(name: str, ref_date):
    return CurveRegistry.get(name, ref_date)


__all__ = ["get_curve"]