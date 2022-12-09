# def greet_person(name='your name'):
#     '''
#     DOCSTRING: this returns a greeting
#     INPUT: name
#     OUTPUT: hello...name
#     '''
#
#     print('this is all body of a function')
#     print('hey there')
#     print('hello ' + name + " this is a greeting...")

# greet_person('Quinn')
# greet_person()

# def remainder(num1, num2):
#     """
#     INPUT: num1, num2 - these are the numbers to divide to get a remainder with %
#
#     """
#     return num1 % num2
#
# print(remainder(10, 3))

# *args and *kwargs

result = sum((1, 2, 3, 4, 5))
print(result)

# my_list = [1, 2, 3, 4, 5]
# my_list[0] = 17
# for i in range (0, len(my_list) - 1):
#     print(my_list[i])

def my_sum(a,b,c,d):
    return sum((a, b, c, d))

print(my_sum(1, 2, 3, 4))

def mysum(*args):
    return sum((args))

print(mysum(1, 2, 3, 4, 4, 5, 6, 7))

def key_value_func(**kwargs):
    print(kwargs)
    print(kwargs.keys())
    print(kwargs.values())

key_value_func(name="Quinn", height=160, weight=150)