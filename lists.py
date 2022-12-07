# my_list = [1, 2, 3, 4, 5]
# print(my_list)
# last_value = my_list.pop()
# first_value = my_list.pop(0)
# print(last_value)
# print(first_value)
# print(my_list)
# my_list.append("this is my sentence")
# print(my_list)
# my_list.pop()
# print(my_list)

# my_list.append([10, 11, 12])
# print(my_list)
# my_list.pop()
# print(my_list)
# my_list.reverse()
# print('after reversed: ', my_list)
# another_list = [2, 4, 6, 3, 1, 7, 9, 8, 10]
# another_list.sort()
# print(another_list)
#
# alphabet_list = ['b', 'e', 'd', 'a', 'c']
# print(alphabet_list)
# alphabet_list.sort()
# print('after sorted: ', alphabet_list)
# item_count = len(alphabet_list)
# print('length of list: ', item_count)
alphabet_list = ['b', 'e', 'd', 'a', 'c']
my_list = [1, 2, 3, 4, 5]

another_list = my_list + alphabet_list
my_list.append(alphabet_list)
print(another_list)
print('after appending: ', my_list )

#
# for i in range(0, len(my_list)):
#     print(my_list[i])