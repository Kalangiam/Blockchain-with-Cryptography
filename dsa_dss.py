import Crypto
from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

# Generate DSA key pair
key = DSA.generate(2048)

# Sign a message using the private key
message = b'Hello, World!'
hash_message = SHA256.new(message)
signer = DSS.new(key, 'fips-186-3')
signature = signer.sign(hash_message)

# Verify the signature using the public key
verifier = DSS.new(key.publickey(), 'fips-186-3')
try:
    verifier.verify(hash_message, signature)
    print("The signature is authentic.")
except ValueError:
    print("The signature is not authentic.")
