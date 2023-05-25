import hashlib
import json
import time
class NonSequentialBlock:
    def __init__(self, data, previous_block_hash):
        self.data = data
        self.previous_block_hash = previous_block_hash
        self.timestamp = time.time()
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block = {
            "data": self.data,
            "previous_block_hash": self.previous_block_hash,
            "timestamp": self.timestamp,
            "nonce": self.nonce
        }
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
def add_nonsequential_block(data, block_chain):
    previous_block_hash = None
    if len(block_chain) > 0:
        previous_block_hash = block_chain[-1].hash
    block = NonSequentialBlock(data, previous_block_hash)
    block_chain.append(block)
def verify_nonsequential_block_chain(block_chain):
    for i in range(1, len(block_chain)):
        previous_block = block_chain[i - 1]
        current_block = block_chain[i]
        if previous_block.hash != current_block.previous_block_hash:
            return False
        if current_block.hash != current_block.calculate_hash():
            return False
    return True
block_chain = []
add_nonsequential_block("Hello", block_chain)
add_nonsequential_block("World", block_chain)
add_nonsequential_block("!", block_chain)
print(verify_nonsequential_block_chain(block_chain))
