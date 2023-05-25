from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Generate a random 32-byte key
key = get_random_bytes(32)

# Initialize the cipher with the key and CBC mode
cipher = AES.new(key, AES.MODE_CBC)

# Encrypt a message
message = b"Hello, world!"
ciphertext = cipher.encrypt(pad(message, AES.block_size))

# Decrypt the ciphertext
decrypt_cipher = AES.new(key, AES.MODE_CBC, iv=cipher.iv)
decrypted_message = unpad(decrypt_cipher.decrypt(ciphertext), AES.block_size)

# Print the original message and decrypted message to verify they match
print(message)
print(ciphertext)
print(decrypted_message)

