#6) Distributed Search & Retrieval — Tiny DHT (consistent hashing / Chord-like ring)
import hashlib
from bisect import bisect_right
import threading
import time

def hash_key(s):
    return int(hashlib.sha1(s.encode()).hexdigest(), 16) % 1024

class DHT:
    def _init_(self):
        self.nodes = {}           # position -> node_id
        self.sorted_pos = []
        self.lock = threading.Lock()  

    def add_node(self, node_id):
        pos = hash_key(node_id)
        self.nodes[pos] = node_id
        self.sorted_pos = sorted(self.nodes)

    def put(self, key, value, storage):
        with self.lock:   # prevents race conditions
            pos = hash_key(key)
            idx = bisect_right(self.sorted_pos, pos) % len(self.sorted_pos)
            node_pos = self.sorted_pos[idx]
            node = self.nodes[node_pos]
            storage.setdefault(node, {})[key] = value
            print(f"[PUT] Stored key={key} -> node={node}")

    def get(self, key, storage):
        pos = hash_key(key)
        idx = bisect_right(self.sorted_pos, pos) % len(self.sorted_pos)
        node_pos = self.sorted_pos[idx]
        node = self.nodes[node_pos]
        value = storage.get(node, {}).get(key, None)
        print(f"[GET] Retrieved key={key} from node={node} -> {value}")
        return value

if _name_ == "_main_":
    dht = DHT()

    nodes = ["nodeA", "nodeB", "nodeC"]
    for n in nodes:
        dht.add_node(n)

    storage = {}

    put_threads = []
    put_data = [("apple", "red"), ("banana", "yellow"), ("grapes", "purple"), ("orange", "orange")]

    for key, value in put_data:
        t = threading.Thread(target=dht.put, args=(key, value, storage))
        put_threads.append(t)
        t.start()

    for t in put_threads:
        t.join()

    print("\n--- Parallel Storage Complete ---\n")

    get_threads = []
    keys = ["apple", "banana", "grapes", "orange"]

    for key in keys:
        t = threading.Thread(target=dht.get, args=(key, storage))
        get_threads.append(t)
        t.start()

    for t in get_threads:
        t.join()

    print("\n--- Parallel Retrieval Complete ---"
