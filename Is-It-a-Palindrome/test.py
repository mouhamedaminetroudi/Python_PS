
# The exercise is to implement a function, is_palindrome(s), that checks if a given string s is 
# a palindrome. A palindrome is a word, phrase, or sequence that reads the same backward as forward, 
# ignoring case differences. The provided code contains a logical error because it uses S instead of s
# (the input parameter). The task is likely to identify and correct this error to ensure the function 
# works correctly.

# Input: "Madam"
# Output: True
# Explanation: "Madam" (case-insensitive) is the same when reversed.

# Input: "Hello"
# Output: False
# Explanation: "Hello" is not the same when reversed.

# =====================
from re import S
def is_palindrome(s):
    return S.lower() == S[::-1].lower()
