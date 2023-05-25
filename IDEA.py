from Crypto.Cipher import IDEA 

# Set the encryption key
key = b"secret_k"

# Create an IDEA object
idea = IDEA.new(key)

# Encrypt the data
plaintext = b"Hello, World!"
ciphertext = idea.encrypt(plaintext)

# Decrypt the data
decryptedtext = idea.decrypt(ciphertext)

# Print the results
print("Plaintext: ", plaintext)
print("Ciphertext: ", ciphertext)
print("Decryptedtext: ", decryptedtext)
