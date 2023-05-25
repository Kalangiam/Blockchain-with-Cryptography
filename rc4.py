from Crypto.Cipher import ARC4

# Set the encryption key
key = b"secret_key"
print(len(key))

# Create an RC4 object
cipher = ARC4.new(key)

# Encrypt a message
message = b"Hello, world!"
ciphertext = cipher.encrypt(message)

# Decrypt the message
decrypted_message = cipher.decrypt(ciphertext)
print(len(decrypted_message))

# Print the results
print("Plaintext: ", message)
print("Ciphertext: ", ciphertext)
print("Decrypted message: ", decrypted_message)
