"""Challenge
Min-maxing
Define a function named largest_difference that takes a list of numbers as its only parameter.

Your function should compute and return the difference between the largest and smallest number in the list.

For example, the call largest_difference([1, 2, 3]) should return 2 because 3 - 1 is 2.

You may assume that no numbers are smaller or larger than -100 and 100.
"""


def largest_difference(num_list):
    max = 0
    min = 100
    difference = 0
    for each_number in num_list:
        if each_number > max:
            max = each_number
        if each_number < min:
            min = each_number
    difference = max - min

    return difference

print(largest_difference([1, 2, 3]))