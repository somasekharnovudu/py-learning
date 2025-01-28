
# type will return the data type
print('==== type')
print(type(2))

# range will give the list of result (usefull for numebr iteratoin)
    # 'range' range(5) will be 0 1 2 3 4 (exlucing that number from 0) 
print('==== range')
for elem in range(1,5):
    print(elem)

# enumerate()  for returning the tuple of index and block
list=[1,2,3,4]
for (index,elem) in enumerate(list):
    print('index:')
    print(index)
    print('elem:')
    print(elem)

# str() used to conver non-string to string
number=1
print('==== str()')
print(type(str(number)))

# float used to convert integer to float
print('==== float()')
print(type(float(number)))

#int() used to convert float to integer (will do floor)
print('==== int')
float_num=1.1
print(int(float_num))

# len() will give the length of list or stirng
print('==== len()')
name='soma'
print(len(name))
