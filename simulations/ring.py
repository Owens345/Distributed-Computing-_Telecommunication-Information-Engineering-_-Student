# 13. SELF-STABILIZING TECHNIQUES (Token Ring)
def stabilize(ring):
    """Self-stabilizing algorithm ensuring exactly one token in a ring."""
    while sum(ring) != 1:
        for i in range(len(ring)-1):
            # If two adjacent tokens exist, remove the second
            if ring[i] == 1 and ring[i+1] == 1:
                ring[i+1] = 0
        # If no tokens exist, create one at position 0
        if sum(ring) == 0:
            ring[0] = 1
    return ring

def demo_self_stabilizing():
    """Demonstrate self-stabilizing correction of a token ring system."""
    print("\nSelf-Stabilizing Token Ring Demonstration:")
    ring = [1, 0, 1, 0]  # invalid initial state: two tokens
    print("Before:", ring)
    final = stabilize(ring)
    print("After:", final)