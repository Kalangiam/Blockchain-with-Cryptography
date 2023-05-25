import hashlib
import time

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

class Block:
    def __init__(self, transactions, previous_hash):
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = None

    def generate_hash(self, model='sha256'):
        block_header = str(self.timestamp) + str(self.transactions) + str(self.previous_hash)
        if model == 'sha256':
            block_hash = hashlib.sha256(block_header.encode()).hexdigest()
        elif model == 'md5':
            block_hash = hashlib.md5(block_header.encode()).hexdigest()
        elif model == 'blake2b':
            block_hash = hashlib.blake2b(block_header.encode()).hexdigest()
        else:
            raise ValueError("Invalid hashing model.")
        return block_hash

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block([Transaction(None, None, 0)], "0")

    def add_block(self, transactions, model='sha256'):
        previous_block = self.chain[-1]
        new_block = Block(transactions, previous_block.hash)
        new_block.hash = new_block.generate_hash(model)
        self.chain.append(new_block)

# Create a blockchain instance
blockchain = Blockchain()

# Add some blocks to the blockchain using different hashing models
blockchain.add_block([Transaction("Alice", "Bob", 10), Transaction("Bob", "Charlie", 5)], 'sha256')
blockchain.add_block([Transaction("Charlie", "Alice", 3), Transaction("Bob", "Alice", 2)], 'sha256')
blockchain.add_block([Transaction("Alice", "Charlie", 7), Transaction("Charlie", "Bob", 4)], 'sha256')
blockchain.add_block([Transaction("Bob", "Eve", 8), Transaction("Charlie", "Eve", 3)], 'blake2b')


# Print the blockchain
for block in blockchain.chain:
    print("Block hash:", block.hash)
    for transaction in block.transactions:
        print("Transaction:", transaction.sender, "->", transaction.receiver, ":", transaction.amount)
