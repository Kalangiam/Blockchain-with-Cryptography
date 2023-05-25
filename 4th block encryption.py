           
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
            if block.index==4:
                   key = b'Sixteen byte key'
                   message = str(block.data)
                   byte_message=bytes(message,'utf-8')
                   cipher = AES.new(key, AES.MODE_EAX)
                   nonce = cipher.nonce
                   ciphertext, tag = cipher.encrypt_and_digest(byte_message)
                   print("Data of block_2: ",message)
                   print("ciphertext of block_2: ",ciphertext)
                
           
            else:
                   print("Block no.", block.index, "\n ", "time         : " ,block.timestamp, "\n ","Data         : ", block.data, "\n ","Hash         : ", block.hash, "\n ","Previous_hash: ",block.previous_hash)
                
    def create_transaction_block(self, sender_name, sender_acc_no, beneficiary_name ,beneficiary_acc_no, bank_name, IFSC_code, amount):
        block_index = len(self.chain)
        timestamp = datetime.datetime.now()
        previous_hash = self.chain[-1].hash
        block_data = { "sender_name":sender_name,"sender_acc_no":sender_acc_no, "beneficiary_name":beneficiary_name,"beneficiary_acc_no":beneficiary_acc_no,"bank_name":bank_name,"IFSC_code":IFSC_code, "amount": amount}
        new_block = Block(block_index, timestamp, block_data, previous_hash)
        self.add_block(new_block)

# Example usage
blockchain = Blockchain()
while True:
  blockchain.create_transaction_block(input("sender_name: "),int(input("sender_acc_no: ")),input("beneficiary_name: "),int(input("beneficiary_acc_no: ")),input("bank_name: "),input("IFSC_code: "),float(input("amount (in float): ")))
  blockchain.print_blocks()