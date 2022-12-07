# my_list = [1, 2, 3]
# print(my_list)
# my_list[1] = "NEW VALUE"
# print(my_list)

my_tuple = (1, 2, 3, "some data", ['a', 'b', 'c'], 2, 1, 1, 1)
print(my_tuple)
print(len(my_tuple))
print(my_tuple[3])

my_tuple[4][1] = 'win'
print(my_tuple)
print(my_tuple.count(1))

extracted = my_tuple[3]
print(type(extracted))
print(type(my_tuple))
print(type(my_tuple[0]))

