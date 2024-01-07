import hashlib
import time
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

REWARD = 50  # Set reward for mining a block

class Transaction:
    # Represents a transaction in the blockchain
    def __init__(self, sender, receiver, amount, signature=None):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.signature = signature

    def __repr__(self):
        # Provides a string representation of the transaction
        return f"{self.sender} -> {self.receiver}: {self.amount}"

    def sign_transaction(self, private_key):
        # Signs the transaction using a private RSA key
        h = SHA256.new(str(self).encode('utf-8'))
        self.signature = pkcs1_15.new(private_key).sign(h)

    def is_valid(self):
        # Validates the transaction
        if self.sender == "MINING":
            # Mining transactions don't require a signature
            return True
        if not self.signature or len(self.signature) == 0:
            # Transaction must have a signature
            return False
        h = SHA256.new(str(self).encode('utf-8'))
        try:
            # Verify the signature
            public_key = RSA.import_key(self.sender)
            pkcs1_15.new(public_key).verify(h, self.signature)
            return True
        except (ValueError, TypeError):
            return False

# Mempool to hold transactions before they are added to a block
mempool = []

class Block:
    # Represents a block in the blockchain
    def __init__(self, index, previous_hash, timestamp, transactions, proof_of_work, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.proof_of_work = proof_of_work
        self.hash = calculate_hash(self)

def calculate_hash(block):
    # Calculates the hash of a block
    return hashlib.sha256(f'{block.index}{block.previous_hash}{block.timestamp}{block.transactions}{block.proof_of_work}'.encode('utf-8')).hexdigest()

def proof_of_work(last_proof):
    # Simple Proof of Work algorithm
    proof = last_proof + 1
    while not (proof + last_proof) % 7 == 0:
        proof += 1
    return proof

# Generate RSA keys for the miner and a receiver
miner_key = RSA.generate(2048)
receiver_key = RSA.generate(2048)

# Create a transaction and add it to the mempool
transaction1 = Transaction(miner_key.publickey().exportKey(), receiver_key.publickey().exportKey(), 10)
transaction1.sign_transaction(miner_key)
mempool.append(transaction1)

# Add a block with transactions from mempool
def add_block(prev_block):
    # Creates and returns a new block with transactions from the mempool
    index = prev_block.index + 1
    timestamp = time.time()
    proof = proof_of_work(prev_block.proof_of_work)
    current_transactions = mempool[:10]  # Select up to 10 transactions from mempool
    del mempool[:10]  # Remove these transactions from mempool

    # Add a reward for the miner
    mining_reward = Transaction("MINING", miner_key.publickey().exportKey(), REWARD)
    current_transactions.append(mining_reward)

    hash = calculate_hash(prev_block)
    return Block(index, prev_block.hash, timestamp, current_transactions, proof, hash)

# Initialize blockchain with the genesis block
genesis_block = Block(0, '0', time.time(), [], 0, calculate_hash(Block(0, '0', time.time(), [], 0, '0')))
blockchain = [genesis_block]

# Add a block with transactions from the mempool to the blockchain
new_block = add_block(genesis_block)
blockchain.append(new_block)

# Print the blockchain for demonstration
for block in blockchain:
    print(f"Index: {block.index}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Transactions: {block.transactions}")
    print(f"Hash: {block.hash}\n")
