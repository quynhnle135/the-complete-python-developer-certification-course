# Assignment 1:
"""
    Create a function named merge_lists that accepts 2 lists.
    The function is supposed to merge both of those lists together
    and return the result.
"""

# your code below:
def merge_lists(list1, list2):
    result = list1 + list2
    return result

list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
print(merge_lists(list1, list2))
