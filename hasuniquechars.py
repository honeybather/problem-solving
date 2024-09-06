"""Does word contains unique set of characters?

For example::

    >>> has_unique_chars("Monday")
    True

    >>> has_unique_chars("Moonday")
    False

    >>> has_unique_chars("")
    True

Uppercase and lowercase letters should be considered separately::

    >>> has_unique_chars("Bob")
    True
"""

# empty string  => if not word, return True
# use set to automacilly remove duplicates 
# create a function that will check if the number of char is the sae as it's lenght 
# (number char in word = number char in set)
# so convert the word into a set 
# then compare the lenght of the set w the og word

def has_unique_chars(word):
    """Does word contains unique set of characters?"""

    if not word:
        return True
    
    unique = set(word)
    return len(unique) == len(word)




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. AWESOME!\n")
