"""Does word contain more vowels than non-vowels?

If the word is over half vowels, it should return True:

    >>> has_more_vowels("moose")
    True

If it's half vowels (or less), it's false:

    >>> has_more_vowels("mice")
    False

    >>> has_more_vowels("graph")
    False

Don't consider "y" as a vowel:

    >>> has_more_vowels("yay")
    False

Uppercase vowels are still vowels:

    >>> has_more_vowels("Aal")
    True
"""


# store lowercase & uppercase in a set 
# a string could work but a set has faster lookups

# create a counter for vowels

# loop though each letter in the word
# if letter = vowel, +1

# compare num of vowls > half of lenght of the word

def has_more_vowels(word):
    """Does word contain more vowels than non-vowels?"""

    vowels = set('aioeuAIOEU')
    counter = 0

    for letter in word:
        if letter in vowels:
            counter += 1 

    if counter > len(word)/2:
        return True
    else:
        return False



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. HOORAY!\n")
