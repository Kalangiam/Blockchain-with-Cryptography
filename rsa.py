import Crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate RSA key pair
key = RSA.generate(2048)

# Encrypt a message using the public key
cipher = PKCS1_OAEP.new(key.publickey())
message = b'Hello, World!'
encrypted_message = cipher.encrypt(message)

# Decrypt the message using the private key
decipher = PKCS1_OAEP.new(key)
decrypted_message = decipher.decrypt(encrypted_message)

# Print the original and decrypted message
print('Original message:', message.decode())
print('Decrypted message:', decrypted_message.decode())
