import pytest

from days import days_in_month


@pytest.mark.parametrize(
    "month, expected_days",
    [
        (1, 31),
        (2, 28),
        (3, 31),
        (4, 30),
        (5, 31),
        (6, 30),
        (7, 31),
        (8, 31),
        (9, 30),
        (10, 31),
        (11, 30),
        (12, 31),
    ],
)
def test_days_in_month_common_year(month, expected_days):
    assert days_in_month(month) == expected_days


def test_february_in_leap_year():
    assert days_in_month(2, leap_year=True) == 29


@pytest.mark.parametrize("month", [0, 13, -1])
def test_days_in_month_rejects_invalid_months(month):
    with pytest.raises(ValueError):
        days_in_month(month)