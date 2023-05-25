import random

# Choose a prime number and a primitive root
p = 23
g = 5

# Alice chooses a secret random number a
a = random.randint(1, p-1)

# Bob chooses a secret random number b
b = random.randint(1, p-1)

# Calculate A and B
A = pow(g, a, p)
B = pow(g, b, p)

# Exchange A and B over the insecure channel

# Alice calculates the shared secret key
s_a = pow(B, a, p)

# Bob calculates the shared secret key
s_b = pow(A, b, p)

# Verify that the shared keys are the same
assert s_a == s_b

print("Shared key:", s_a)
