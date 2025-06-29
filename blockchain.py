import hashlib
import time

class Block:
    def __init__(self, index, prev_hash, data, timestamp, difficulty):
        self.index = index
        self.prev_hash = prev_hash
        self.data = data
        self.timestamp = timestamp
        self.difficulty = difficulty
        self.nonce, self.hash = self.mine_block()

    def calculate_hash(self, nonce):
        """
        Menghitung hash block dengan SHA-1.
        """
        text = f"{self.index}{self.prev_hash}{self.data}{self.timestamp}{nonce}"
        return hashlib.sha1(text.encode()).hexdigest()

    def mine_block(self):
        """
        Loop mining: cari nonce yang hash-nya diawali sejumlah 0 sesuai difficulty.
        """
        nonce = 0
        while True:
            hash_result = self.calculate_hash(nonce)
            if hash_result.startswith('0' * self.difficulty):
                print(f"[Mined] Nonce: {nonce} | Hash: {hash_result}")
                return nonce, hash_result
            nonce += 1

class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty

    def create_genesis_block(self):
        print("[Genesis] Mining genesis block...")
        return Block(0, "0", "Genesis Block Zcashon", time.time(), self.difficulty)

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, data):
        print(f"[Mining] Block #{len(self.chain)} ...")
        prev_block = self.get_last_block()
        new_block = Block(
            index=len(self.chain),
            prev_hash=prev_block.hash,
            data=data,
            timestamp=time.time(),
            difficulty=self.difficulty
        )
        self.chain.append(new_block)

    def display_chain(self):
        print("\n=== Zcashon (ZHON) Blockchain ===")
        for block in self.chain:
            print(f"Index     : {block.index}")
            print(f"Prev Hash : {block.prev_hash}")
            print(f"Hash      : {block.hash}")
            print(f"Nonce     : {block.nonce}")
            print(f"Data      : {block.data}")
            print(f"Timestamp : {block.timestamp}")
            print("-" * 50)

if __name__ == "__main__":
    # Contoh jalankan blockchain Zcashon
    zhon_chain = Blockchain(difficulty=4)

    zhon_chain.add_block("Block 1 Data")
    zhon_chain.add_block("Block 2 Data")
    zhon_chain.add_block("Block 3 Data")

    zhon_chain.display_chain()
