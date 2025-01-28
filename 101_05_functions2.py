blockchain = []


def get_last_item(list):
    return list[-1]


def append_data(new_item, last_item=[1]):
    """ Append the data

    Arguments:
        :new_item: Item to add to exising list: mandatory
        :last_item: last item of chain (default [1])

    """
    blockchain.append([last_item, float(new_item)])


append_data(1, [0])
append_data(input('Please enter amount:\n'))
append_data(input('Please enter amount:\n'))
append_data(input('Please enter amount:\n'))
print(blockchain)
