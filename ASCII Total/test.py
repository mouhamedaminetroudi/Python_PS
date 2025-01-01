# Description:
# You'll be given a string, and have to return the sum of all characters as an int. The function should be able to handle all printable ASCII characters.

# Examples:

# uniTotal("a") == 97
# uniTotal("aaa") == 291

# ==============
def uniTotal(string):
    # Use sum with ord to calculate the total Unicode value of all characters
    return sum(ord(char) for char in string)