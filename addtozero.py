"""Given list of ints, return True if any two nums in list sum to 0.

    >>> add_to_zero([])
    False

    >>> add_to_zero([1])
    False

    >>> add_to_zero([1, 2, 3])
    False

    >>> add_to_zero([1, 2, 3, -2])
    True

Given the wording of our problem, a zero in the list will always
make this true, since "any two numbers" could include that same
zero for both numbers, and they sum to zero:

    >>> add_to_zero([0, 1, 2])
    True
"""

# Rita's thought process:

# we need to check if there are any two numbers in a list that sum to zero
# if a positive number is present, we need to check if a negetive one is also present

# we'll use a set to store the numbers
# convert list to a set (fast lookups)
# iterate through the list and check if the 'negation' of each number is in the set
# if it is, return True,  else return False

# create set : convert list to set_nums
# loop : for each num in nums
#           check if negation of num is in set_nums
#           if it is, return True
#  return False

def add_to_zero(nums):
    """Given list of ints, return True if any two nums sum to 0."""

    set_nums = set(nums) 
    # we'll convert the list of numbers into a set

    for num in nums:
        # iterate through each number in the original list
        if -num in set_nums:
            # check if the negative of the current number exists in the set
            # if it does, that means we have found two numbers that sum to zero
            return True
    return False


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. NOTHING ESCAPES YOU!\n")
