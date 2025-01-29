
# type will return the data type
print('==== type')
print(type(2))

# range will give the list of result (usefull for numebr iteratoin)
# 'range' range(5) will be 0 1 2 3 4 (exlucing that number from 0)
print('==== range')
for elem in range(1, 5):
    print(elem)

# enumerate()  for returning the tuple of index and block
list = [1, 2, 3, 4]
for (index, elem) in enumerate(list):
    print('index:')
    print(index)
    print('elem:')
    print(elem)

# str() used to conver non-string to string
number = 1
print('==== str()')
print(type(str(number)))

# float used to convert integer to float
print('==== float()')
print(type(float(number)))

# int() used to convert float to integer (will do floor)
print('==== int')
float_num = 1.1
print(int(float_num))

# len() will give the length of list or stirng
print('==== len()')
name = 'soma'
print(len(name))

# range selector [1:2] gets the range with start included and end excluded
# if we put -1 it will be from last index -1 will remove last 1 elem, -2 will remove last 2 elements
# it shallow clones only
list = [1, 2, 3]
print(list[1:2])


list = [1, 2, 3, -5]
is_positive = [ele >= 0 for ele in list]
print('===== is positive', is_positive)
print('==== all', all(is_positive))
print('==== any', any(is_positive))

