"""Challenge
Palindrome
A string is a palindrome when it is the same when read backwards.

For example, the string "bob" is a palindrome. So is "abba". But the string "abcd" is not a palindrome, because "abcd" != "dcba".

Write a function named palindrome that takes a single string as its parameter. Your function should return True if the string is a palindrome, and False otherwise.
"""
def palindrome(any_string):
    reverse_string = any_string[::-1]
    print(any_string)
    print(reverse_string)
    if reverse_string == any_string:
        return True
    else:
        return False

print(palindrome("bob"))