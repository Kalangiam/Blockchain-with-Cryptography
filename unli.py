import hashlib
import json

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def to_dict(self):
        return {"sender": self.sender, "recipient": self.recipient, "amount": self.amount}

    def encode(self):
        return json.dumps(self.to_dict(), sort_keys=True).encode()

class Block:
    def __init__(self, previous_block_hash, transactions):
        self.previous_block_hash = previous_block_hash
        self.transactions = transactions
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({"transactions": [tx.to_dict() for tx in self.transactions], "nonce": self.nonce, "previous_block_hash": self.previous_block_hash}, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()

        print("Block mined:", self.hash)

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2

    def create_genesis_block(self):
        return Block("0", [])

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_block_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
    

if __name__ == "__main__":
    blockchain = Blockchain()

    # Add transactions

while True:

    

    # Create block
    block = Block("", )
    blockchain.add_block(block)

    # Print blockchain
    for block in blockchain.chain:
        print("Block hash:", block.hash)
        print("Previous block hash:", block.previous_block_hash)
        for tx in block.transactions:
            print("Transaction:", tx.to_dict())
