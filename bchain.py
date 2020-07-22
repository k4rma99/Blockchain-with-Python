from time import time
import hashlib
import json


class Block:
    def __init__(self):
        pass

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.transactions = []

    def new_block(self,proof,previous_hash = None): # Creates a new block and adds into chain

        """
            Creates a new block in the Blockchain

            :param proof : <int> Proof given by the Proof Of Work Function
            :paramm previous_hash : <str> Hash of previous block
            :return : <dict> New Block


        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]), #Given hash or hash value of last appended block
        }

        self.transactions = [] # New block transactions are resetted

        self.chain.append(block)

        return block


    def new_transaction(self, sender, recipient , amount): # Creates a new transaction and adds into list of transactions
        
        """
            Creates a new transaction to enter the next mined block

            :param sender: <str> Adrress of sender
            :param recipient : <str> Address of recipient
            :param amount : <int> Amount in transaction
            :return <int> : Index of block that holds the transaction

        """

        self.current_transaction.append({'sender' : sender, 'recipient' : recipient, 'amount' : amount })

        return self.last_block['index'] + 1
        
        pass

    @staticmethod
    def hash(block): #Hashes a block 
        
        """
            A SHA256 hash of a block

            :param block: <dict> Block
            :return : <str>


        """

        block_string = json.dumps(block, sort_keys = True).encode()  #Ordered dictionary to prevent inconsistent hashes

        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self): # Returns ;ast elements of a block
        return self.chain[-1]