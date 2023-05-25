import hashlib

# Define the message to be hashed
message = b"Hello, worlkn;kvnlxnlkxh;y;xlfklkxjglxjljoxihjfgnmxoihoughoklnmxklnfkgd!"

# Hash the message using SHA-256
hash_object = hashlib.sha256(message)
hash_value = hash_object.digest()

# Print the hash value as a hexadecimal string
print(hash_value.hex())
