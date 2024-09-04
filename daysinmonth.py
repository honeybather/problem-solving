"""How many days are there in a month?

Given a string with a month and a year (separated by a space),
returns the number of days in that month.

For example::

    >>> for i in range(1, 13):
    ...     date = str(i) + " 2016"
    ...     print("%s has %s days." % (date, days_in_month(date)))
    1 2016 has 31 days.
    2 2016 has 29 days.
    3 2016 has 31 days.
    4 2016 has 30 days.
    5 2016 has 31 days.
    6 2016 has 30 days.
    7 2016 has 31 days.
    8 2016 has 31 days.
    9 2016 has 30 days.
    10 2016 has 31 days.
    11 2016 has 30 days.
    12 2016 has 31 days.

    >>> days_in_month("02 2015")
    28
"""


def is_leap_year(year):
    """Is this year a leap year?

    Every 4 years is a leap year::

        >>> is_leap_year(1904)
        True

    Except every hundred years::

        >>> is_leap_year(1900)
        False

    Except-except every 400::

        >>> is_leap_year(2000)
        True
    """

    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    if year % 4 == 0:
        return True

# leap year determines if Feb has 29 or 28 days
# input: a string "M YYYY"
# output: int of days in month

# steps:
# 1. extract the month and year separately, use split
# 2. they will still be strings, convert to int
# 3. for february (2), check if leap year, return 29 or 28
# 4. return 31 for months in [1,3,5,7,8,10,12] else return 30

def days_in_month(date):
    """How many days are there in a month?"""

    # split date into month and year
    month, year = date.split()
    # convert month and year to int
    month = int(month)
    year = int(year)

    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    
    if month in [1,3,5,7,8,10,12]:
        return 31
    else:
        return 30


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. W00T!\n")

