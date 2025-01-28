name = input('Please enter your name: ')
age = int(input('Please enter your age: '))

decade_lived = 0


def calculate_decades(age):
    """Calculates the number of decades based on age"""
    return age // 10


def log_user_details(name, age):
    global decade_lived
    decade_lived = calculate_decades(age)
    print('Hi '+name+', You have lived ' + str(decade_lived) + ' decades')


log_user_details(name, age)

print('====== decades '+str(decade_lived))


list = [1, 2, 3, 4]
print(len(list))
