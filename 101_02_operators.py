# arthematic operators
# +, - , *, /(will give float), **(power), //(will give integer), %

num1 = 10
num2 = 20
print('====== +')
print(num1+num2)
# can also use like num+=2

print('====== -')
print(num1-num2)

print('====== *')
print(num1*num2)

print('====== /')
print(num1/2)

print('====== **')
print(num1**2)

print('====== //')
print(num1//2)

# string operatos
# + (Concatanation) * (repetition)

name1 = 'SOMA'
name2 = 'SEKHAR'
print('===== string concat')
print(name1+' '+name2)

print('==== string repetition')
print(name1*5)

# compare operators

# ==, != ,>=, <=, > , < is, in

print('===== =')
print(1 == 1)

print('===== !=')
print(1 != 2)

print('===== >=')
print(1 >= 1)

print('===== <=')
print(1 == 1)

print('===== is')  # compares reference of objects
list = [1, 2, 3]
list2 = list
print(list is list2)

print('===== in')  # checks existance of element in list
print(1 in [1, 2, 3])
