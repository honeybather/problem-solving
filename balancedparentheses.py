"""Does a string have balanced parentheses?

For example::

   >>> has_balanced_parens("()")
   True

   >>> has_balanced_parens("(Oh Noes!)(")
   False

   >>> has_balanced_parens("((There's a bonus open paren here.)")
   False

   >>> has_balanced_parens(")")
   False

   >>> has_balanced_parens("(")
   False

   >>> has_balanced_parens("(This has (too many closes.) ) )")
   False

If you receive a string with no parentheses, consider it balanced::

   >>> has_balanced_parens("Hey...there are no parens here!")
   True
"""

# check for every opened and closed parentheses
# so check every char in the string/phrase
# keep track of the parentheses call it, parens_count

def has_balanced_parens(phrase):
    """Does a string have balanced parentheses?"""

    parens_count = 0

    for char in phrase:
        # if it's an opened, + 1
        if char == '(':
            parens_count += 1
        # if it's a closed one, - 1 bcuz we went it to b 0 to ensure balence
        elif char == ')':
            parens_count -= 1

            # if at any moment it becomes negative, automically false 
            if parens_count > 0:
                return False
    
    # if the tracker equals to 0, all is good
    return parens_count == 0



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY PARENS!\n")
