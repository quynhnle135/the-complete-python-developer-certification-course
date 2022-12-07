my_list = ['b', 'd', 'a', 'z', 'x']
another_list = [1, 2, 3, 4, 5]

# get last three elements from my_list and last three elements from another list
# combine them, sorted in reversed
my_list.sort()
my_list.reverse()
another_list.sort()
another_list.reverse()
result = my_list[2:] + another_list[2:]

print(result)