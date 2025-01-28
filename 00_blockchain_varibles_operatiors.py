
# variable types
#  Numbers (Integers and Float), String, Boolean

num = 1

num2 = 20.0

name = 'soma'

is_there = True


# operators
# Arthematic on number
# +(Sum), - (diff), *(Multiply), / (devide till number), //(devide till float), ** (power), % (will give reminder)

print('== Addition')
print(1+2)
print('== Subtraction')
print(1-2)
print('== multplication')
print(2*3)
print('== devide till float')
print(2/3)
print('== device till integer')
print(2//3)
print('== power')
print(2**3)
print('== remainder')
print(3 % 2)

# + on a string is to concat them
print('==== string concatanation')
print('Hi '+',There!')

# * on a string to repeat the stirng n times
print('Repeat me! ' * 10)


# compare operators ==, !=, >=, <=, >, <, is, in
# == checks for value and is checks for same reference of objects
# in check for availablity of elemment in a list
# not is like ! to be used only with is or in or in loop condition

print('==== chekcing ==')
print(1 == 1)
print('==== chekcing !=')
print(1 != 2)
print('==== chekcing >=')
print(1 >= 2)
print('==== chekcing <=')
print(1 <= 2)

list1 = [1, 2]
list2 = list1
list3 = [1, 2]
print('===== is Value #1')
print(list1 is list2)
print('===== is Value #2')
print(list1 is list3)
print('===== == on list')
print(list1 == list3)
print('===== in list')
print(1 in list1)
print('====== not')
print(not True)


# boolean operators "and" "or"
print('==== and')
print(True and False)

print('==== or')
print(True or False)

# grouping conditions
# and will take importance first and or will be next
age = 29
if name == 'soma' and age < 20 or age > 30:
    print('==== Yes')
    # Here and will be executed first and Above statement becomes False or age>30 which becomes False or True and lastly True

# if we want grouping the use paranthesys
if name == 'soma' and (age < 20 or age > 30):
    print('==== Yes')
else:
    print('==== No')
