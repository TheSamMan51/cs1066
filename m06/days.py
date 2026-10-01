### m06/days.py

def days_in_month(month, leap_year=False):
    if month < 1 or month > 12:
        raise ValueError("month must be between 1 and 12")

    if month == 2:
        if leap_year:
            return 29
        return 28

    if month in [4, 6, 9, 11]:
        return 30

    return 31
