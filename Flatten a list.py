"""Challenge
Flatten a list
Write a function that takes a list of lists and flattens it into a one-dimensional list.

Name your function flatten. It should take a single parameter and return a list.

For example, calling:

flatten([[1, 2], [3, 4]])
Should return the list:

[1, 2, 3, 4]
"""


def flatten(two_dimentional_list):
    final_list = []

    for x in range (0, len(two_dimentional_list)):
        a = two_dimentional_list[x]
        for y in range (0, len(a)):
            final_list.append(a[y])
    return final_list
print(flatten([[1, 2], [3, 4]]))