blockchain = []


def get_last__transaction(list):
    list_length = len(list)
    if list_length >= 1:
        return list[-1]
    return None


def append_data(new_item, last_item):
    """ Append the data
    Arguments:
        :new_item: Item to add to exising list: mandatory
        :last_item: last item of chain (default [1])
    """
    if last_item == None:
        blockchain.append([[1], float(new_item)])
    else:
        blockchain.append([last_item, float(new_item)])


def get_user_input():
    inputvalue = float(input('Please enter amount: '))
    return inputvalue


def get_user_choice():
    inputValue = input('Your choice: ')
    return inputValue


while (True):
    print('Please choose:')
    print('1. Enter new value')
    print('2. Print current block chain')
    print('q. Exit the program')
    accepted_values = ['1', '2', '3']

    user_choice = get_user_choice()

    if user_choice == '1':
        tax_amount = get_user_input()
        append_data(tax_amount, get_last__transaction(blockchain))
    elif user_choice == '2':
        for block in blockchain:
            print('outputing blocks')
            print(block)
    elif user_choice == 'q':
        break
    else:
        print('Input invalid, Please choose again!')
    print('Choice registered')


print('Created blocks: ' + str(len(blockchain)))

print('Done!')


# There is no switch statement