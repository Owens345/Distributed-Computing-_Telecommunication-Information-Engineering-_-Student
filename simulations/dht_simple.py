#6) Distributed Search & Retrieval — Tiny DHT (consistent hashing / Chord-like ring)
import hashlib
from bisect import bisect_right

def hash_key(s):
    return int(hashlib.sha1(s.encode()).hexdigest(),16) % 1024

class DHT:
    def __init__(self):
        self.nodes = {}  # pos -> node_id
        self.sorted_pos = []

    def add_node(self, node_id):
        pos = hash_key(node_id)
        self.nodes[pos] = node_id
        self.sorted_pos = sorted(self.nodes)

    def put(self, key, value, storage):
        pos = hash_key(key)
        idx = bisect_right(self.sorted_pos, pos) % len(self.sorted_pos)
        node_pos = self.sorted_pos[idx]
        node = self.nodes[node_pos]
        storage.setdefault(node, {})[key] = value
        print(f"Stored key={key} -> node={node}")

    def get(self, key, storage):
        pos = hash_key(key)
        idx = bisect_right(self.sorted_pos, pos) % len(self.sorted_pos)
        node_pos = self.sorted_pos[idx]
        node = self.nodes[node_pos]
        return storage.get(node, {}).get(key, None)

if __name__ == "__main__":
    dht = DHT()
    nodes = ["nodeA","nodeB","nodeC"]
    for n in nodes: dht.add_node(n)
    storage = {}
    dht.put("apple","red", storage)
    dht.put("banana","yellow", storage)
    print("get apple:", dht.get("apple", storage))
    print("get banana:", dht.get("banana", storage))