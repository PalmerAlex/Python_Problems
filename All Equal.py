"""Challenge
All equal
Define a function named all_equal that takes a list and checks whether all elements in the list are the same.

For example, calling all_equal([1, 1, 1]) should return True."""


def all_equal(any_list):
    count = 0
    for x in range(len(any_list)):
        if any_list[x] == any_list[x-1]:
            count = count + 1

        previous = any_list[x]

    if count == len(any_list):
        return True
    return False


print(all_equal([]))
