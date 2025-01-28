genesis_block = {
    'previous_hash': 'xyz',
    'transactions': [],
    'index': 0
}
blockchain = [genesis_block]
open_transactions = []
owner = 'soma'


def get_last__transaction(list):
    list_length = len(list)
    if list_length >= 1:
        return list[-1]
    return None


def add_transaction(reciepiant, amount=1.0, sender=owner):
    """ Append the data
    Arguments:
        :sender: Item to add to exising list: mandatory
        :reciepiant: last item of chain (default [1])
        :amount:
    """
    new_transaction = {
        'sender': sender,
        'reciepiant': reciepiant,
        'amount': amount
    }
    open_transactions.append(new_transaction)


def mine_block():
    last_block = blockchain[-1]
    hash_block = '-'.join([str(last_block[key]) for key in last_block])
    print(hash_block)
    # for keys in last_block:
    #     value = last_block[keys]
    #     hash_string = hash_string + str(value)
    block = {
        'previous_hash': str(hash_block),
        'transactions': open_transactions,
        'index': len(blockchain)
    }
    blockchain.append(block)
    open_transactions.clear()


def get_user_input():
    tx_reciever = input('Please enter reciever name: ')
    tax_amount = float(input('Please enter amount: '))
    # Tuple: Tuple is ordered data with duplicates allowes and order matters
    return (tx_reciever, tax_amount)


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
    print('1. add new transaction')
    print('2. Print current block chain')
    print('h. Manipulate the block chain')
    print('m. Mine the block chain')
    print('q. Exit the program')
    accepted_values = ['1', '2', '3']

    user_choice = get_user_choice()
    print(user_choice)
    if user_choice == '1':
        reciever, amount = get_user_input()
        add_transaction(reciever, amount)
        print(open_transactions)
    elif user_choice == '2':
        for block in blockchain:
            print('outputing blocks')
            print(block)
    elif user_choice == 'q':
        continue_loop = False
    elif user_choice == 'm':
        mine_block()
    else:
        print('Input invalid, Please choose again!')
else:  # else can be used in loops as well which will execute after the loop completed but when loop 'break'ed
    print('==== user left')

print('Done!')
