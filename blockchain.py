import hashlib
import json
from time import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_data = []

        # Create the genesis block
        self.create_block(previous_hash='1')

    def create_block(self, previous_hash):
        block = Block(
            index=len(self.chain),
            previous_hash=previous_hash,
            timestamp=time(),
            data=self.current_data,
            hash=self.calculate_hash(len(self.chain), previous_hash, time(), self.current_data)
        )
        self.current_data = []
        self.chain.append(block)

    def add_data(self, data):
        self.current_data.append(data)

    @staticmethod
    def calculate_hash(index, previous_hash, timestamp, data):
        return hashlib.sha256(f"{index}{previous_hash}{timestamp}{json.dumps(data)}".encode('utf-8')).hexdigest()

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != self.calculate_hash(
                current_block.index, current_block.previous_hash, current_block.timestamp, current_block.data
            ):
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True
