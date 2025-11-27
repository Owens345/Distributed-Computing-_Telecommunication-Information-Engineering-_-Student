#2) Consensus — Simple majority-based consensus (toy Raft-like vote phase)
import threading, queue, time, random

class Node(threading.Thread):
    def __init__(self, nid, inboxes):
        super().__init__()
        self.nid = nid
        self.inboxes = inboxes
        self.proposal = random.choice(["A","B","C"])
        self.votes = {}
        self.decision = None

    def run(self):
        # Broadcast proposal
        for q in self.inboxes:
            q.put(("PROP", self.nid, self.proposal))
        # receive proposals and vote
        time.sleep(0.1 * random.random())
        while not self.decision:
            try:
                msg = self.inboxes[self.nid].get(timeout=0.5)
            except queue.Empty:
                break
            typ, sender, payload = msg
            if typ == "PROP":
                # simple vote: accept if payload == my proposal else maybe accept with prob
                vote = 1 if payload == self.proposal else (1 if random.random() < 0.4 else 0)
                for q in self.inboxes:
                    q.put(("VOTE", self.nid, (payload, vote)))
            elif typ == "VOTE":
                val, v = payload
                self.votes.setdefault(val, 0)
                self.votes[val] += v
                # if any value has majority, decide
                if self.votes[val] > len(self.inboxes)//2:
                    self.decision = val
                    for q in self.inboxes:
                        q.put(("DECIDE", self.nid, val))
            elif typ == "DECIDE":
                self.decision = payload
        print(f"Node {self.nid} proposed {self.proposal} -> decided {self.decision}")

if __name__ == "__main__":
    N = 7
    queues = [queue.Queue() for _ in range(N)]
    nodes = [Node(i, queues) for i in range(N)]
    for n in nodes: n.start()
    for n in nodes: n.join()