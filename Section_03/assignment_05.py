# Assignment 5:

"""
Define a function called key_list_items that can accept an unlimited number
of lists along with another argument. The function should return
the second_folder to last item in the specific list specified by the user of the function.

Example:

    For example, the below function call should return: jan

    key_list_items("people", things=['book', 'tv'], people=['pete', 'mike', 'jan', 'tom'])

"""

# Your Code Below:
def key_list_items(key, **kwargs):
    key = kwargs[key]
    return key[-2]

print(key_list_items("people", things=['book', 'tv'], people=['pete', 'mike', 'jan', 'tom']))