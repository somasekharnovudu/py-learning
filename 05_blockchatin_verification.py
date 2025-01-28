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


def verify_chain():
    is_valid = True
    for block_index in range(len(blockchain)):
        block = blockchain[block_index]
        if block_index == 0:
            continue
        if block[0] != blockchain[block_index-1]:
            is_valid = False
            break
    else:
        print('-' * 20)
    #  the below also works and above one is using 'range' range(5) will be 0 1 2 3 4 (exlucing that number from 0) 
    #  or range(5,10) will be 5 6 7 8 9
    # or range(1,20,2) will be 1, 3, 5,...19 i.e 2 will be step for iteration
    # for block in blockchain:
    #     if block_index == 0:
    #         block_index += 1
    #         continue
    #     if block[0] != blockchain[block_index-1]:
    #         is_valid = False
    #         break
    #     block_index += 1
    # else:
    #     print('-' * 20)
    return is_valid
 

continue_loop = True

while (continue_loop):
    print('Please choose:')
    print('1. Enter new value')
    print('2. Print current block chain')
    print('h. Manipulate the block chain')
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
        continue_loop = False
    elif user_choice == 'h':
        if len(blockchain) > 1:
            blockchain[0] = [2]
    else:
        print('Input invalid, Please choose again!')
    if not verify_chain():
        print('==== Block Invalid!')
        break
else:  # else can be used in loops as well which will execute after the loop completed but when loop 'break'ed
    print('==== user left')

print('Done!')
