#9. MEMBERSHIP AND FAILURE DETECTION (Heartbeat Simulation)
import time

nodes = {
    "Node1": time.time(),
    "Node2": time.time(),
    "Node3": time.time()
}

def heartbeat(node):
    """Simulate receiving a heartbeat signal from a node by updating its last-seen time."""
    nodes[node] = time.time()

def detect_failures(timeout=3):
    """Detect failed nodes based on absence of heartbeat within a time threshold."""
    now = time.time()
    failed = []
    for node, last_seen in nodes.items():
        if now - last_seen > timeout:
            failed.append(node)
    return failed

def demo_failure_detection():
    """Demonstrate failure detection by simulating a heartbeat timeout."""
    print("\nFailure Detection Demonstration:")
    time.sleep(4)  # Exceed timeout threshold intentionally
    failures = detect_failures()
    print("Failed nodes:", failures)
