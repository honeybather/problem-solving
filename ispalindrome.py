"""Is this word a palindrome?

    >>> is_palindrome("a")
    True

    >>> is_palindrome("noon")
    True

    >>> is_palindrome("racecar")
    True

    >>> is_palindrome("porcupine")
    False

Treat spaces and uppercase letters normally:

    >>> is_palindrome("Racecar")
    False
"""

# reverse string using slicing
# word[::-1] reverses the string.
# if og word is = to its reversed version, return True.



def is_palindrome(word):
    """Return True/False if this word is a palindrome."""
    return word == word[::-1]


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!")
