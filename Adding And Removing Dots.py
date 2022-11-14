"""
Challenge
Adding and removing dots
Write a function named add_dots that takes a string and adds "." in between each letter. For example, calling add_dots("test") should return the string "t.e.s.t".

Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. For example, calling remove_dots("t.e.s.t") should return "test".

If both functions are correct, calling remove_dots(add_dots(string)) should return back the original string for any string.

(You may assume that the input to add_dots does not itself contain any dots.)
"""

def add_dots(any_string):
    final_string = ""

    for x in range(0, len(any_string)):
        if x == len(any_string) -1 :
            final_string = final_string + any_string[x]
        else:
            final_string = final_string + any_string[x] + "."
    return final_string
def remove_dots(any_string):
    final_string = ""
    for letter in  any_string:
        if letter != ".":
            final_string = final_string + letter

    return final_string


print(add_dots("test"))
print(remove_dots(".t.e.s.t."))