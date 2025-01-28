blockchain = []


def get_last_item(list):
    return list[-1]


def append_data(new_item, last_item=[1]):
    blockchain.append([last_item, new_item])
    print(blockchain)


append_data(1, [0])
append_data(2)
append_data(3)
append_data(4)
append_data(last_item=2, new_item=1) # keyword arguments
