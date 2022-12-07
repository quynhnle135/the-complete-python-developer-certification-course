dict = {'k1': 'some data',
        'k2': 'hello',
        7 : 'Quinn'}
# print(dict)
# print(len(dict))
# print(dict.values())
# print(dict.keys())
# print(dict['k1'])
# dict['k2'] = 'seventeen'
# dict[7] = 'NEW VALUE'
# print(dict)


# print(people_weight_dict)
# print(people_weight_dict['john'])
# people_weight_dict['john'] = 100
# weight_of_mike = people_weight_dict.pop('mike')
# print(weight_of_mike)
# print(people_weight_dict)
# people_weight_dict.clear()
# print(people_weight_dict)

# people_weight_dict['brooklyn'] = 500
# print(people_weight_dict)
people_weight_dict = {'john' : 140, 'robert' : 165,
                      'paul' : 200, 'mike' : 250, 'items' : ['oranges', 'bananas', 'strawberries',
                      {'k1': 'quinn'}],
                      'tuples' : (1, 2, 3, 4)}

print(people_weight_dict)
print(people_weight_dict['items'][0])
print(people_weight_dict['items'][2])
print(people_weight_dict['items'][3]['k1'])
print(people_weight_dict['tuples'][2])
print(people_weight_dict)
people_weight_dict.pop('tuples')
people_weight_dict.pop('items')
print(people_weight_dict)
