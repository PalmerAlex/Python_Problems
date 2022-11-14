"""Challenge
Consecutive zeros
The goal of this challenge is to analyze a binary string consisting of only zeros and ones. Your code should find the biggest number of consecutive zeros in the string. For example, given the string:

"1001101000110"
The biggest number of consecutive zeros is 3.

Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones. Your function should return the number described above.
"""

def consecutive_zeros(any_string):
    max_num_zero = 0
    max_this_time = 0

    for x in range (0, len(any_string)):
        if any_string[x] == "0":
            max_this_time = max_this_time +1

        if any_string[x] == "1":
            max_this_time = 0;
        if max_num_zero < max_this_time:
            max_num_zero = max_this_time


    return max_num_zero

print(consecutive_zeros("1001101000110"))
