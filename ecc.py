import ecdsa
import hashlib

# Generate ECC key pair
sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
vk = sk.get_verifying_key()

# Sign a message using the private key
message = b'Hello, World!'
hash_message = hashlib.sha256(message).digest()
signature = sk.sign(hash_message)

print("private key: ",sk.to_string().hex())
print("public key: ",vk.to_string().hex())
print("signature:  ",hash_message.hex())
print("message: ",message.decode())
print("private key: ",sk.compress_point())

# Verify the signature using the public key
try:
    assert vk.verify(signature, hash_message)
    print("The signature is authentic.")
except AssertionError:
    print("The signature is not authentic.")
    
    
