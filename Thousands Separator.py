"""Challenge
Thousands separator
Write a function named format_number that takes a non-negative number as its only parameter.

Your function should convert the number to a string and add commas as a thousands separator.

For example, calling format_number(1000000) should return "1,000,000".
"""


def format_number(non_negative):
    non_negative_as_string = str(non_negative)
    reverse_string = non_negative_as_string[::-1]
    final_string = ""
    count = 0
    for x in range(0, len(reverse_string)):
        count+= 1
        final_string += reverse_string[x]
        if count == 3 and x != len(reverse_string)-1:
            final_string += ","
            count = 0;
    final_string = final_string[::-1]
    return final_string


print(format_number(10009903289235728375982357982357298572990909090000))
