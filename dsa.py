# from Crypto.Cipher import AES
# import hashlib
# import datetime

# class Bank:
#     def __init__(self):
#         self.accounts = {}

#     def add_account(self, name, balance):
#         self.accounts[name] = balance

#     def transfer(self, sender, receiver, amount, blockchain, key):
#         if sender not in self.accounts or receiver not in self.accounts:
#             return "Invalid account"
#         if self.accounts[sender] < amount:
#             return "Insufficient balance"
#         self.accounts[sender] -= amount
#         self.accounts[receiver] += amount
#         transaction_data = f"{sender} transferred {amount} to {receiver}"
#         encrypted_data = self.encrypt_data(transaction_data, key)
#         blockchain.add_block(encrypted_data)
#         return "Transaction successful"

#     def encrypt_data(self, data, key):
#         cipher = AES.new(key, AES.MODE_EAX)
#         nonce = cipher.nonce
#         ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))
#         return nonce + ciphertext + tag

#     def decrypt_data(self, data, key):
#         nonce = data[:16]
#         ciphertext = data[16:-16]
#         tag = data[-16:]
#         cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
#         plaintext = cipher.decrypt_and_verify(ciphertext, tag)
#         return plaintext.decode('utf-8')

# class Block:
#     def __init__(self, data, previous_hash):
#         self.timestamp = datetime.datetime.now()
#         self.data = data
#         self.previous_hash = previous_hash
#         self.hash = self.calculate_hash()

#     def calculate_hash(self):
#         sha = hashlib.sha256()
#         sha.update(str(self.timestamp).encode('utf-8') +
#                    str(self.data).encode('utf-8') +
#                    str(self.previous_hash).encode('utf-8'))
#         return sha.hexdigest()

# class Blockchain:
#     def __init__(self):
#         self.chain = [self.create_genesis_block()]

#     def create_genesis_block(self):
#         return Block("Genesis Block", "0")

#     def add_block(self, data):
#         previous_block = self.chain[-1]
#         new_block = Block(data, previous_block.hash)
#         self.chain.append(new_block)

#     def is_chain_valid(self):
#         for i in range(1, len(self.chain)):
#             current_block = self.chain[i]
#             previous_block = self.chain[i-1]
#             if current_block.hash != current_block.calculate_hash():
#                 return False
#             if current_block.previous_hash != previous_block.hash:
#                 return False
#         return True
    
    
    
    
    
from Crypto.Cipher import DES
import hashlib
import datetime

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, name, balance):
        self.accounts[name] = balance

    def transfer(self, sender, receiver, amount, blockchain, key):
        if sender not in self.accounts or receiver not in self.accounts:
            return "Invalid account"
        if self.accounts[sender] < amount:
            return "Insufficient balance"
        self.accounts[sender] -= amount
        self.accounts[receiver] += amount
        transaction_data = f"{sender} transferred {amount} to {receiver}"
        encrypted_data = self.encrypt_data(transaction_data, key)
        blockchain.add_block(encrypted_data)
        return "Transaction successful"

    def encrypt_data(self, data, key):
        cipher = DES.new(key, DES.MODE_ECB)
        padded_data = self.pad_data(data)
        ciphertext = cipher.encrypt(padded_data.encode('utf-8'))
        return ciphertext

    def decrypt_data(self, data, key):
        cipher = DES.new(key, DES.MODE_ECB)
        plaintext = cipher.decrypt(data)
        unpadded_data = self.unpad_data(plaintext.decode('utf-8'))
        return unpadded_data

    def pad_data(self, data):
        padding_length = 8 - (len(data) % 8)
        padding = chr(padding_length) * padding_length
        return data + padding

    def unpad_data(self, data):
        padding_length = ord(data[-1])
        return data[:-padding_length]

class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8'))
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

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True
    
    
    
    
    
    
# from Crypto.PublicKey import RSA
# from Crypto.Cipher import PKCS1_OAEP
# import hashlib
# import datetime

# class Bank:
#     def __init__(self):
#         self.accounts = {}

#     def add_account(self, name, balance):
#         self.accounts[name] = balance

#     def transfer(self, sender, receiver, amount, blockchain, public_key):
#         if sender not in self.accounts or receiver not in self.accounts:
#             return "Invalid account"
#         if self.accounts[sender] < amount:
#             return "Insufficient balance"
#         self.accounts[sender] -= amount
#         self.accounts[receiver] += amount
#         transaction_data = f"{sender} transferred {amount} to {receiver}"
#         encrypted_data = self.encrypt_data(transaction_data, public_key)
#         blockchain.add_block(encrypted_data)
#         return "Transaction successful"

#     def encrypt_data(self, data, public_key):
#         rsa_key = RSA.import_key(public_key)
#         cipher = PKCS1_OAEP.new(rsa_key)
#         ciphertext = cipher.encrypt(data.encode('utf-8'))
#         return ciphertext

#     def decrypt_data(self, data, private_key):
#         rsa_key = RSA.import_key(private_key)
#         cipher = PKCS1_OAEP.new(rsa_key)
#         plaintext = cipher.decrypt(data)
#         return plaintext.decode('utf-8')

# class Block:
#     def __init__(self, data, previous_hash):
#         self.timestamp = datetime.datetime.now()
#         self.data = data
#         self.previous_hash = previous_hash
#         self.hash = self.calculate_hash()

#     def calculate_hash(self):
#         sha = hashlib.sha256()
#         sha.update(str(self.timestamp).encode('utf-8') +
#                    str(self.data).encode('utf-8') +
#                    str(self.previous_hash).encode('utf-8'))
#         return sha.hexdigest()

# class Blockchain:
#     def __init__(self):
#         self.chain = [self.create_genesis_block()]

#     def create_genesis_block(self):
#         return Block("Genesis Block", "0")

#     def add_block(self, data):
#         previous_block = self.chain[-1]
#         new_block = Block(data, previous_block.hash)
#         self.chain.append(new_block)

#     def is_chain_valid(self):
#         for i in range(1, len(self.chain)):
#             current_block = self.chain[i]
#             previous_block = self.chain[i-1]
#             if current_block.hash != current_block.calculate_hash():
#                 return False
#             if current_block.previous_hash != previous_block.hash:
#                 return False
#         return True
