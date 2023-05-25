import hashlib
from Crypto.Cipher import DES
import Crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.data).encode('utf-8') + str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block("Genesis Block", "0")

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(data, previous_block.hash)
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

# Create a new blockchain
my_blockchain = Blockchain()

# Add some sample transactions
transaction_data =b"{'sender_account': '123456789','recipient_account': '987654321','amount': 100.0,'date': '2023-04-12'}"
key = b'abcdefgh'
plaintext = transaction_data
plaintext += b'\0' * (8 - len(plaintext) % 8)
cipher = DES.new(key, DES.MODE_ECB)
ciphertext = cipher.encrypt(plaintext)
my_blockchain.add_block = cipher.decrypt(ciphertext)


# Print the blockchain
for block in my_blockchain.chain:
    print("Data:", block.data)
    print("Hash:", block.hash)
    print("Previous Hash:", block.previous_hash)
    print()
   
   
   
   
   
