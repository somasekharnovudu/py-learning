# Lists
# Array like: Odered items, can have duplicates ex: [1,2] and can manipulate and can be of different data types
lst = [1, 2, 'soma']
print(lst)
print(type(list))

# Tuples, sets and Dictionaries
# Tuples: Orderd items can have duplicates and cannot manipulate(like constants) ex: ("soma",31) can be of different data types
tple = ('soma', 21)
print(tple)
print(type(tple))

# sets: un-ordered, have only keys as values and to be unique and can be of diff data types ex: {'soma','31'}
st = {'soma', 31}
print(st)
print(type(st))

# Dictionaries: Object like: Un-oredered items, with key-value pair , unique keys and can be of diff data type ex: {'name':'soma','age':31}
dict = {'name': 'soma', 'age': 31}
print(dict)
print(type(dict))
# in Dictionaries keys should be in quotes '' or ""

## iterable Functions & Behaviours

# List comphrensions
# to do operations over list elements
numbers = [1, 2, 3]
number2 = [elem * 2 for elem in numbers]
print(number2)

# Dictionary comphrensions
# can be used to convert list of tuples to dictionary
tupllist = [('name', 'soma'), ('age', 30)]
user = {key: value for (key, value) in tupllist}
print(user)


# list comprensions with if condition (can be used to filter or and apply logic only to certain elements)
numbers = [1, 2, 3, 4, 5, 6]
numbers2 = [el for el in numbers if el % 2 == 0]  # filters only even
numbers2 = [el * 2 for el in numbers if el %
            2 == 0]  # filters and doubles only even

print(number2)

