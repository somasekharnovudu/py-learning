blockchain = [[1]]


def get_last__transaction(list):
    return list[-1]


def append_data(new_item, last_item=[1]):
    """ Append the data
    Arguments:
        :new_item: Item to add to exising list: mandatory
        :last_item: last item of chain (default [1])
    """
    blockchain.append([last_item, float(new_item)])


def get_user_input():
    inputvalue = float(input('Please enter amount:'))
    return inputvalue


tax_amount = get_user_input()
append_data(tax_amount, get_last__transaction(blockchain))

tax_amount = get_user_input()
append_data(tax_amount, get_last__transaction(blockchain))

tax_amount = get_user_input()
append_data(tax_amount, get_last__transaction(blockchain))

for block in blockchain:
    print('outputing blocks')
    print(block)

print('Done printing')
