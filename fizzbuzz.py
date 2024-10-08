"""Count from 1 to 20 in fizzbuzz fashion.

Loop from 1 to 20 (inclusive). Each through, if the number
is evenly divisible by 3, say 'fizz'. If the number is evenly
divisible by 5, say 'buzz'. If the number is evenly divisible
by both 3 and 5, say 'fizzbuzz'. Otherwise, say the number.

    >>> fizzbuzz()
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    17
    fizz
    19
    buzz
"""

# Loop from 1 to 20 (inclusive) == range(1,21)

# if number is divisible by 3 and 5 print out 'fizzbuzz'
# else if (elif) number is divisible by 3 print out 'fizz'
# else if (elif) number is divisible by 5 print out 'buzz'
# else print number 

def fizzbuzz():
    """Count from 1 to 20 in fizzbuzz fashion."""

    for num in range(1,21):
        if num % 3 == 0 and num % 5 == 0:
            print('fizzbuzz')
        elif num % 3 == 0:
            print('fizz')
        elif num % 5 == 0:
            print('buzz')
        else:
            print(num)
    


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. FIZZBUZZ FOR THE WIN!\n")
