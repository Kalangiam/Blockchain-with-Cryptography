from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
# Set the encryption key
key = b'secret_k'

# Create a DES object
des = DES.new(key, DES.MODE_ECB)

# Encrypt the data
plaintext = b'Hello, World!'
ciphertext = des.encrypt(plaintext)

# Decrypt the data
decryptedtext = des.decrypt(ciphertext)

# Print the results
print("Plaintext: ", plaintext)
print("Ciphertext: ", ciphertext)
print("Decryptedtext: ", decryptedtext)
# from Crypto.Cipher import DES

# key = 'hello123'

# def pad(text):
#         while len(text) % 8 != 0:
#             text += ''
#         return text

# des = DES.new(key, DES.MODE_ECB)

# text1 = 'Python is the Best Language!'

# padded_text = pad(text1)

# encrypted_text = des.encrypt(padded_text)

# print(encrypted_text)

# print(des.decrypt(encrypted_text))



