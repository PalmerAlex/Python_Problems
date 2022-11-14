#Challenge
#Middle letter
#Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

#For example, mid("abc") should return "b" and mid("aaaa") should return "".


# aaa mid because odd

# aaaa no mid because no even

def mid(any_string):
    mod = len(any_string) % 2
    if mod != 0:
        middle_index = len(any_string)//2
        return any_string[middle_index]
    return ""

print(mid("aba"))

