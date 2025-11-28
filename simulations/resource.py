12. RESOURCE ALLOCATION AND AUCTION ALGORITHMS
# Medium-Length Demonstration (Functional + Formal)
import random

class AuctionSystem:
    """
    A simplified auction-based resource allocation system.
    Each participant bids for available distributed resources,
    and the highest bidder wins the resource.
    """

    def _init_(self, resources, participants):
        """
        Initialize resources and participants.
        :param resources: dict mapping resource → units
        :param participants: list of participant names
        """
        self.resources = resources
        self.participants = participants
        self.bids = {}           # {participant: {resource: bid_value}}
        self.allocations = {}    # {resource: winner}

    def generate_bids(self, min_bid=1, max_bid=10):
        """
        Automatically generate random bids for demonstration.
        This simulates sealed-bid behavior.
        """
        for p in self.participants:
            self.bids[p] = {}
            for r in self.resources:
                self.bids[p][r] = random.randint(min_bid, max_bid)

    def run_auction(self):
        """
        Allocate each resource to the highest bidder.
        Ties are broken by alphabetical order for fairness.
        """
        for resource in self.resources:
            highest = -1
            potential_winners = []

            # Find the highest bid
            for p in self.participants:
                bid = self.bids[p][resource]
                if bid > highest:
                    highest = bid
                    potential_winners = [p]
                elif bid == highest:
                    potential_winners.append(p)

            # Tie-breaker
            winner = sorted(potential_winners)[0]
            self.allocations[resource] = winner

    def show_bids(self):
        """Display all bids submitted by participants."""
        print("\nBIDS SUMMARY")
        for p in self.bids:
            print(f"{p}: {self.bids[p]}")

    def show_allocations(self):
        """Display final resource allocation results."""
        print("\nFINAL ALLOCATIONS")
        for resource, winner in self.allocations.items():
            print(f"{resource} → {winner}")

