# 11. DISTRIBUTED TRANSACTION ALGORITHMS (Two-Phase Commit)
class Participant:
    """Represents a participant in a distributed transaction."""
    def __init__(self, name, will_commit=True):
        self.name = name
        self.will_commit = will_commit

    def prepare(self):
        """Return whether this participant approves the commit."""
        return self.will_commit

class Coordinator:
    """Coordinator that manages the two-phase commit protocol."""
    def __init__(self, participants):
        self.participants = participants

    def two_phase_commit(self):
        """Run two-phase commit: prepare phase followed by commit/abort."""
        print("\nTwo-Phase Commit Demonstration:")
        print("Phase 1: Prepare")
        for p in self.participants:
            if not p.prepare():
                print("Abort Transaction (Participant", p.name, "cannot commit)")
                return
        print("Phase 2: Commit")
        print("Transaction successfully committed.")

def demo_two_phase_commit():
    """Demonstrate the two-phase commit protocol with participants."""
    p1 = Participant("P1")
    p2 = Participant("P2", will_commit=False)
    coord = Coordinator([p1, p2])
    coord.two_phase_commit()