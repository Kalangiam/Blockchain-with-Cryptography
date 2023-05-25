from Crypto.Cipher import AES  
import math
import hashlib
import datetime

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, datetime.datetime.now(), "Genesis Block", "0")

    def add_block(self, new_block):
        new_block.previous_hash = self.chain[-1].hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def print_blocks(self):
        for block in self.chain:
            if block.index==4:
                   key = b'Sixteen byte key'
                   message = str(block.data)
                   byte_message=bytes(message,'utf-8')
                   cipher = AES.new(key, AES.MODE_EAX)
                   nonce = cipher.nonce
                   ciphertext, tag = cipher.encrypt_and_digest(byte_message)
                   print("Data of block_2: ",message)
                   print("ciphertext of block_2: ",ciphertext)

    def create_transaction_block(self, transactions):
        block_index = len(self.chain)
        timestamp = datetime.datetime.now()
        previous_hash = self.chain[-1].hash
        block_data = {"transactions": transactions}
        new_block = Block(block_index, timestamp, block_data, previous_hash)
        self.add_block(new_block)

# Example usage
blockchain = Blockchain()
while True:
  blockchain.create_transaction_block(input())
  blockchain.print_blocks()