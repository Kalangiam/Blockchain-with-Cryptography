import hashlib
class Block:
  def __init__(self,data,prev_hash):
    self.data = data 
    self.prev_hash = prev_hash
    self.hash= self.hash_calc()
  def hash_calc(self):
    sha = hashlib.sha256()
    sha.update(self.data.encode())
    return sha.hexdigest()

class Blockchain:
  def __init__(self):
    self.chain = [self.Genesis_Block()]
  def Genesis_Block(self):
    return Block("new block","0")
  def add_block(self,data):
    prev_block = self.chain[-1]
    new_block = Block(data,prev_block.hash)
    self.chain.append(new_block)


blockchain=Blockchain()

blockchain.add_block("second block")
blockchain.add_block("third block")
blockchain.add_block("fourth block")
blockchain.add_block("fifth block")
blockchain.add_block("sixth block")



print('blockchain: ' )

for block in blockchain.chain:
  print('Data: ',block.data)
  print('previous hash: ',block.prev_hash)
  print('hash',block.hash)
  print()


