genesis_block = {
    'previous_hash': 'xyz',
    'transactions': [],
    'index': 0
}
blockchain = [genesis_block]
open_transactions = []
owner = 'soma'
participants = {'max', 'soma'}
MINING_REWARD = 10


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
    if verify_transaction(sender, amount):
        open_transactions.append(new_transaction)
        participants.add(sender)
        participants.add(reciepiant)
        return True
    return False


def verify_transaction(sender, tx_amount):
    (sent_amt, recieved_amt, balance) = get_balance(sender)
    return balance >= tx_amount


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


def get_balance(participant):
    """Returns amount sent,recieved,balance tuple"""
    tx_sender = [[transactions['amount'] for transactions in block['transactions']
                  if transactions['sender'] == participant] for block in blockchain]
    tx_sender_open = [tx['amount']
                      for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(tx_sender_open)

    amount_sent = 0
    for block_transaction in tx_sender:
        for amount in block_transaction:
            if not amount:
                continue
            else:
                amount_sent += amount

    tx_reciever = [[transactions['amount'] for transactions in block['transactions']
                    if transactions['reciepiant'] == participant] for block in blockchain]

    amount_recieved = 0
    for block_transaction in tx_reciever:
        for amount in block_transaction:
            if not amount:
                continue
            else:
                amount_recieved += amount
    return amount_sent, amount_recieved, amount_recieved-amount_sent


def mine_block():
    global open_transactions
    last_block = blockchain[-1]
    last_block_hash = hash_block(last_block)
    reward_transaction = {
        'sender': 'MINING',
        'reciepiant': owner,
        'amount': MINING_REWARD
    }
    copied_transcations = open_transactions[:]
    open_transactions.append(reward_transaction)
    block = {
        'previous_hash': str(last_block_hash),
        'transactions': copied_transcations,
        'index': len(blockchain)
    }
    blockchain.append(block)
    open_transactions = []


def get_user_input():
    tx_reciever = input('Please enter reciever name: ')
    tax_amount = float(input('Please enter amount: '))
    # Tuple: Tuple is ordered data with duplicates allowes and order matters
    return (tx_reciever, tax_amount)


def get_user_choice():
    inputValue = input('Your choice: ')
    return inputValue


def verify_chain():
    for (index, block) in enumerate(blockchain):
        if (index == 0):
            continue
        if block['previous_hash'] != hash_block(blockchain[index-1]):
            return False
    return True


def validate_transactions():
    return all([verify_transaction(tx['sender'], tx['amount']) for tx in open_transactions])


continue_loop = True

while (continue_loop):
    print('Please choose:')
    print('1. add new transaction')
    print('2. Print current block chain')
    print('3. Check transaction validity')
    print('p. Print participants')
    print('h. Manipulate the block chain')
    print('m. Mine the block chain')
    print('q. Exit the program')
    accepted_values = ['1', '2', '3']

    user_choice = get_user_choice()
    print(user_choice)
    if user_choice == '1':
        reciever, amount = get_user_input()
        tx_status = add_transaction(reciever, amount)
        if not tx_status:
            print('==== Transaction FAILED! No balance')
            continue
        print(open_transactions)
    elif user_choice == '2':
        for block in blockchain:
            print('outputing blocks')
            print(block)
    elif user_choice == 'h':
        blockchain[0] = {
            'previous_hash': 'xyz',
            'transactions': [{'sender': 'chris', 'reciepiant': 'max', 'amount': 10.0}],
            'index': 0
        }
    elif user_choice == 'q':
        continue_loop = False
    elif user_choice == 'm':
        mine_block()
    elif user_choice == 'p':
        print(participants)
    elif user_choice == '3':
        if validate_transactions():
            print('Transactions are valid')
        else:
            print('Transcations are not valid')
    else:
        print('Input invalid, Please choose again!')
    if not verify_chain():
        print('==== Invalid chain')
        break
    user_balance = get_balance('soma')
    print('==== user balance')
    print(user_balance)
else:  # else can be used in loops as well which will execute after the loop completed but when loop 'break'ed
    print('==== user left')

print('Done!')
