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
print(message.decode())
print(decrypted_message.decode())
'''Note that you should always use a secure random key generator to generate the key for AES encryption, as using a weak key can compromise the security of your encryption. The get_random_bytes() method from the Crypto.Random module provides a secure way to generate random keys.

Also note that it is important to use padding to ensure that the message is a multiple of the block size (16 bytes for AES). The pad() method from the Crypto.Util.Padding module is used to add padding to the message, and the unpad() method is used to remove padding from the decrypted message.'''