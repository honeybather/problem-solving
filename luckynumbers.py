"""Return n unique random numbers from 1-10 (inclusive).

Given the numbers 1-10, return `n` random numbers, making sure
to never return the same number twice. You can trust that this
function will never be called with n < 0 or n > 10.

It's tricky to test random functions! However, we can make sure
asking for zero numbers gives us an empty list::

    >>> lucky_numbers(0)
    []

And if we ask for all numbers, we shouldn't get any repeats::

    >>> sorted(lucky_numbers(10))
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""

import random
# this lets me use python's random module

# return list of random numbers bewteen 1 and 10
# if (n) is 0 return empty list
# no repeats

# use random.sample  
# use range(1,11) = (start,stop) inclusive
# n: how many random numbers we need to pick


def lucky_numbers(n):
    """Return n unique random numbers from 1-10 (inclusive)."""

    return random.sample(range(1,11), n)    


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** RITA IS THE SMARTEST!\n")
