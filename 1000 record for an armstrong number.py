           
from Crypto.Cipher import AES            
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
          
          for i in range(0,1000):
            num = i
            sum = 0
            temp = num
            while temp > 0:
                digit = temp % 10
                sum += digit ** 3
                temp //= 10
              
            if num==sum:   
                   key = b'Sixteen byte key'
                   message = str(block.data)
                   byte_message=bytes(message,'utf-8')
                   cipher = AES.new(key, AES.MODE_EAX)
                   nonce = cipher.nonce
                   ciphertext, tag = cipher.encrypt_and_digest(byte_message)
                   print(i,"is an armstong number","Data: ",message)
                   print("ciphertext armstrong block: ",ciphertext)
            else :
                  continue
       
                
                
    def create_transaction_block(self):
        block_index = len(self.chain)
        timestamp = datetime.datetime.now()
        previous_hash = self.chain[-1].hash
        block_data = {}
        new_block = Block(block_index, timestamp, block_data, previous_hash)
        self.add_block(new_block)

# Example usage
blockchain = Blockchain()
blockchain.print_blocks()