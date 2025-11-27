#5) Fault-Tolerance Techniques — Primary-backup replication + failover
import threading, time, random

class Replica:
    def __init__(self, name):
        self.name = name
        self.state = {}
        self.alive = True

    def apply(self, key, value):
        self.state[key] = value

def primary_loop(primary, backups):
    seq = 0
    while seq < 8:
        if not primary.alive:
            print("Primary failed!")
            break
        key = f"k{seq}"
        val = f"v{seq}"
        print(f"[Primary] applying {key}={val}")
        primary.apply(key,val)
        # replicate to backups
        for b in backups:
            if b.alive:
                b.apply(key,val)
        time.sleep(0.2)
        seq += 1

def failover(backups):
    time.sleep(0.7)
    # kill primary externally in this demo
    return

if __name__ == "__main__":
    p = Replica("P")
    backups = [Replica("B1"), Replica("B2")]
    # simulate primary crash after some time
    t = threading.Thread(target=primary_loop, args=(p, backups))
    t.start()
    time.sleep(0.5)
    p.alive = False  # crash
    t.join()
    # elect new primary (first alive backup)
    new_primary = next((b for b in backups if b.alive), None)
    print("New primary:", new_primary.name, "state:", new_primary.state)