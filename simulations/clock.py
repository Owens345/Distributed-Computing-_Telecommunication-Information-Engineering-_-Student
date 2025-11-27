# 10. CLOCK SYNCHRONIZATION ALGORITHMS (Lamport Clocks)
class Process:
    """A process implementing Lamport logical clock rules."""
    def __init__(self):
        self.clock = 0

    def event(self):
        """Increment clock to represent an internal event."""
        self.clock += 1
        print("Internal event → Clock:", self.clock)

    def send(self):
        """Increment clock before sending a message and return timestamp."""
        self.clock += 1
        print("Send message → Clock:", self.clock)
        return self.clock

    def receive(self, incoming_clock):
        """Update local clock based on received timestamp."""
        self.clock = max(self.clock, incoming_clock) + 1
        print("Receive message → Clock:", self.clock)

def demo_lamport_clock():
    """Demonstrate Lamport logical clocks with simulated send/receive events."""
    print("\nLamport Clock Demonstration:")
    p1 = Process()
    p2 = Process()
    msg = p1.send()
    p2.receive(msg)