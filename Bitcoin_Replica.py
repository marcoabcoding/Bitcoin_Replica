#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import hashlib
import time
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

REWARD = 50  # Seting reward for mining a block

class Transaction:
    # Represents a transaction in the blockchain
    def __init__(self, sender, receiver, amount, signature=None):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.signature = signature

    def __repr__(self):
        # Representation of the transaction for easy readability
        return f"{self.sender} -> {self.receiver}: {self.amount}"

    def sign_transaction(self, private_key):
        # Signs the transaction with a private key
        h = SHA256.new(str(self).encode('utf-8'))
        self.signature = pkcs1_15.new(private_key).sign(h)

    def is_valid(self):
        # Checks if the transaction is valid
        if self.sender == "MINING":
            # Mining transactions are always valid
            return True
        if not self.signature or len(self.signature) == 0:
            # Invalid if there's no signature
            return False
        h = SHA256.new(str(self).encode('utf-8'))
        try:
            # Verify the transaction signature
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
    # Proof of Work algorithm: find a number that, combined with the last proof, is divisible by 7
    proof = last_proof + 1
    while not (proof + last_proof) % 7 == 0:
        proof += 1
    return proof

# Generate RSA keys for a miner and a receiver
miner_key = RSA.generate(2048)
receiver_key = RSA.generate(2048)

# Create a transaction and add it to the mempool
transaction1 = Transaction(miner

