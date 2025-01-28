
num_arr = [1, 2, 3]

for item in num_arr:
    print(item) # prints actual item
    print(num_arr.index(item)) # prints index


user_obj = {'name': 'soma', 'age': 30}

for item in user_obj:
    print(item) # prints key
    print(user_obj[item]) # prints value