import random

# INSTRUCTIONS

# Access Python from you CLI

# Type help() or for example help(str)


# <QUESTION 1>

# Given a string, return a string where for every char in the original string, there are three chars.

# <EXAMPLES>

# one("The") → "TTThhheee"
# one("AAbb") → "AAAAAAbbbbbb"
# one("Hi-There") → "HHHiii---TTThhheeerrreee"

# <HINT>
# How does a for loop iterate through a string?


def one(string):
    result = []
    for char in string:
      
        result.append(char)
        result.append(char)

        result.append(char)
    return "".join(result)

    # <QUESTION 2>
    #  Write a function which returns the boolean True if the input is only divisible by one and itself.
    # The function should return the boolean False if not.
    # <EXAMPLES>
    # two(3) → True
    # two(8) → False
    # <HINT>
    # What operator will give you the remainder?
    # Use your CLI to access the Python documentation and get help manipulating strings - help(range).


def two(num):
    result = True
    for i in range(num):
      if i != 0 and i != 1:
        if num % i == 0:
            result = False
    return result

    # <QUESTION 3>

    # Write a function which takes an integer input, a, and returns the sum a+aa+aaa+aaaa.

    # So if 2 was the input, the function should return 2+22+222+2222 which is 2468.

    # <EXAMPLES>

    # three(9) → 11106
    # three(5) → 6170

    # <HINT>
    # What happens if you multiply a string by a number?


def three(a):
    m_list = []
    #for  in range(4):
        
    #    if i > 0:
    mini_string = ""
    for i in range(4):
                # mini_string = ""
        mini_string += str(a)

        m_list.append(mini_string)
    
    result = 0
    for number in m_list:
        result += int(number)
    return result

    # <QUESTION 4>

    # Given two Strings of equal length, 'merge' them into one String.

    # Do this by 'zipping' the Strings together.

    # Start with the first char of the first String.
    # Then add the first char from the second String.
    # Then add the second char from the first String.
    # And so on.

    # Maintain case.

    # You will not encounter whitespace.

    # <EXAMPLES>

    # four("String","Fridge") → "SFtrriidngge"
    # four("Dog","Cat") → "DCoagt"
    # four("True","Tree") → "TTrrueee"
    # four("return","letter") → "rleettutrenr"

    # <HINT>
    # Use your CLI to access the Python documentation and get help manipulating strings - help(list.insert).
    # How would you seperate a string into characters?


def four(string1, string2):
    string1_list = list(string1)
    string2_list = list(string2)
    result = []

    for i in range(len(string1_list)):
        result.append(string1_list[i])
        result.append(string2_list[i])

    #result = zip(string1_list, string2_list)

    return "".join(result)

    # <QUESTION 5>

    # Write a function to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

    # <EXAMPLES>

    # five() → [100,102,122,198,200]
    # five() → [108,104,106,188,200]
    # five() → [154,102,132,178,164]

    # <HINT>
    # There is a module which can be used to generate random numbers, this module is called random.
    # The random module contains a function called randint.


def five():
    result = []
    while len(result) < 5:
        result.append(random.randrange(100, 200, 2))

    return result

    # <QUESTION 6>

    # Given a string, return the boolean True if it ends in "py", and False if not.
    # Ignore Case.
    # For Example:
    # six("ilovepy") → True
    # six("welovepy") → True
    # six("welovepyforreal") → False
    # six("pyiscool") → False

def six(string):
    n_string = string.lower()

    if n_string[-2:] == "py":
        return True
    return False

    # <QUESTION 7>

    # Given three ints, a b c, one of them is small, one is medium and one is large.

    # Return the boolean True if the three values are evenly spaced, so the
    # difference between small and medium is the same as the difference between
    # medium and large.

    # Do not assume the ints will come to you in a reasonable order.

    # <EXAMPLES>

    # seven(2, 4, 6) → True
    # seven(4, 6, 2) → True
    # seven(4, 6, 3) → False
    # seven(4, 60, 9) → False

    # <HINT>
    # There is a function for lists called sort.
    # Use the cli to access the documentation help(list.sort)


def seven(a, b, c):
    int_list = [a,b,c]
    sorted_list = sorted(int_list)
    if sorted_list[2] - sorted_list[1] == sorted_list[1] - sorted_list[0]:
        return True

    return False 

    # <QUESTION 8>

    # Given a string and an integer, n, return a string that removes n letters from the 'middle' of the string.

    # The string length will be at least n, and be odd when the length of the input is odd, so there will always be a 'middle'.

    # <EXAMPLES>

    # eight("Hello", 3) → "Ho"
    # eight("Chocolate", 3) → "Choate"
    # eight("Chocolate", 1) → "Choclate"

    # <HINT>
    # Use the cli to access the documentation help(str.replace)


def eight(string, num):
    return

    # <QUESTION 9>

    # Given two string inputs, if one can be made from the other return the boolean True, if not return the boolean False.

    # <EXAMPLES>

    # nine("god", "dog") → True
    # nine("tree", "tiredest") → True
    # nine("cat", "dog") → False
    # nine("tripping", "gin") → True

    # <HINT>
    # There are no hints for this question.


def nine(string1, string2):
    # make sure string1 is the shortest of the two
    shortest_string = ""
    longer_string = ""
    result = True
    if len(string1) <= len(string2):
        shortest_string = string1
        longer_string = string2
    else:
        shortest_string = string2
        longer_string = string1

    for char in shortest_string:
        if char not in longer_string:
            result = False

    return result

    # <QUESTION 10>

    # Write a function which takes 2 integers greater than 0, X,Y as input and generates a 2-dimensional array.

    # The element value in the i-th row and j-th column of the array should be i*j.

    # <EXAMPLES>

    # ten(3,2) → [[0,0,0],[0,1,2]]
    # ten(2,1) → [[0,0]]
    # ten(3,4) → [[0,0,0],[0,1,2],[0,2,4],[0,3,6]]

    # <HINT>
    # Think about nesting for loops.


def ten(a, b):
    return