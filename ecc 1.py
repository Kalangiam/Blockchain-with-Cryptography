from Crypto.PublicKey import ECC
pk= ECC.generate(curve='P-256')
vk= pk.public_key()
message