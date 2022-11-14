"""Challenge
Anagrams
Two strings are anagrams if you can make one from the other by rearranging the letters.

Write a function named is_anagram that takes two strings as its parameters. Your function should return True if the strings are anagrams, and False otherwise.

For example, the call is_anagram("typhoon", "opython") should return True while the call is_anagram("Alice", "Bob") should return False.
"""
def is_anagram(first_string,second_string):
    str1 = first_string.lower()
    str2 = second_string.lower()
    if len(str1) == len(str2):

        str1 = sorted(str1)
        str2 = sorted(str2)

        if str1 == str2:
            return True
        else:
            return False


print(is_anagram("typhoon", "opython"))
