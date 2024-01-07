# Bitcoin Replica in Python

This repository contains a Python-based replica of a Bitcoin-like blockchain. It is designed to demonstrate the concepts of blockchain technology, especially those used in cryptocurrencies like Bitcoin.

## Features

- **Blockchain Technology**: Implements a basic version of the blockchain, a distributed ledger technology.
- **Transactions**: Ability to create digital transactions, similar to how cryptocurrencies work.
- **Digital Signing**: Transactions are digitally signed using RSA keys.
- **Proof of Work**: Implements a simple proof of work algorithm to validate new blocks.
- **Mining Rewards**: Miners are rewarded with digital currency for their efforts in validating transactions and creating new blocks.

## How It Works

1. **Transaction Creation**: Transactions are created between parties, digitally signed, and added to a mempool.
2. **Block Creation**: Blocks are created from transactions in the mempool, including a reward for the miner.
3. **Proof of Work**: A proof of work algorithm secures the creation of new blocks.
4. **Chain Formation**: Blocks are chained together, forming the blockchain with each block referencing its predecessor.

## Running the Script

To run this script, you need Python installed on your system along with the `Crypto` library for RSA key generation and signing.

1. Clone the repository.
2. Run the script: `python bitcoin_replica.py`.

## Educational Purpose

This project serves as an educational tool for those interested in understanding the basics of blockchain technology and cryptocurrencies like Bitcoin. It is not a real cryptocurrency but a demonstration of the underlying principles.

## Requirements

- Python 3
- PyCryptodome (`pip install pycryptodome` for RSA key generation and signing)

Note: This implementation is simplified and not intended for production use. It serves as a learning aid to understand the workings of blockchain technology.
