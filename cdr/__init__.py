def get_calendar(name: str):
    from cdr.calendar import CalendarRegistry
    return CalendarRegistry.get(name)


__all__ = ["get_calendar"]