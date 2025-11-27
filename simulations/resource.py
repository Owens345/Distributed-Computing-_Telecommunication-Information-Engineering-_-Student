def demo_auction_allocation():
    """Demonstrate simple auction-based resource allocation via highest bids."""
    print("\nAuction-Based Allocation Demonstration:")
    bids = {"AppA": 5, "AppB": 2, "AppC": 8}
    sorted_bids = sorted(bids.items(), key=lambda x: -x[1])
    for app, bid in sorted_bids:
        print(app, "→ Bid:", bid)