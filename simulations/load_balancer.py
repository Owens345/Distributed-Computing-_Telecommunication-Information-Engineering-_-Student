#4) Load Balancing Strategies — Round-robin & Least-connections simulation
import random, time
from collections import deque

class Backend:
    def __init__(self, name):
        self.name = name
        self.conn = 0
    def handle(self, duration):
        self.conn += 1
        time.sleep(duration * 0.001)
        self.conn -= 1

def simulate(lb_strategy, requests, backends):
    for req in requests:
        if lb_strategy == "rr":
            # simple round robin
            i = simulate.rr_idx % len(backends)
            simulate.rr_idx += 1
            backends[i].handle(req)
            print(f"RR -> {backends[i].name} (req {req})")
        elif lb_strategy == "least":
            b = min(backends, key=lambda x: x.conn)
            b.handle(req)
            print(f"LeastConn -> {b.name} (req {req})")
simulate.rr_idx = 0

if __name__ == "__main__":
    backends = [Backend(f"S{i}") for i in range(3)]
    requests = [random.randint(1,10) for _ in range(12)]
    print("=== Round Robin ===")
    simulate("rr", requests, backends)
    print("\n=== Least Connections ===")
    simulate("least", requests, backends)