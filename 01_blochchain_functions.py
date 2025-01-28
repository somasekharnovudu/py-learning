blockchain = []

def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    return blockchain[-1]


def append_data(new_item, last_item=[1]):
    """ Append the data
    Arguments:
        :new_item: Item to add to exising list: mandatory
        :last_item: last item of chain (default [1])
    """
    blockchain.append([last_item, float(new_item)])

blockchain.append([1])

append_data(input('Please enter amount:\n'), get_last_blockchain_value())
append_data(input('Please enter amount:\n'), get_last_blockchain_value())
append_data(input('Please enter amount:\n'), get_last_blockchain_value())

print(blockchain)
