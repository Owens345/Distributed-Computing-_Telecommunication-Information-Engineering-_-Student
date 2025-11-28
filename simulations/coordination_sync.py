#1) Coordination & Synchronization — Distributed lock + simple leader election (ring)
import multiprocessing as mp
import time
import random

def process_node(node_id, n, token_pipe_in, token_pipe_out, election_pipe_in, election_pipe_out):
    # leader election: each node sends its id around once; winner is max id
    election_pipe_out.send(node_id)
    elected = None
    while True:
        try:
            candidate = election_pipe_in.recv()
            if candidate > node_id:
                election_pipe_out.send(candidate)
            elif candidate < node_id:
                election_pipe_out.send(node_id)
            else:
                # candidate == node_id means circle completed => leader found
                elected = candidate
                break
        except EOFError:
            break

    print(f"[P{node_id}] leader elected: P{elected}")

    # Mutual exclusion via token passing (token == permission to enter critical section)
    for _ in range(3):
        token = token_pipe_in.recv()
        if token == "TOKEN":
            print(f"[P{node_id}] got TOKEN - entering critical section")
            time.sleep(random()*0.5)
            print(f"[P{node_id}] leaving critical section")
            token_pipe_out.send("TOKEN")
        else:
            token_pipe_out.send(token)

def random():
    return random_module.random()

if __name__ == "__main__":
    import random as random_module
    N = 5
    # pipes for token pass (ring)
    token_pipes = [mp.Pipe(duplex=True) for _ in range(N)]
    # pipes for election (ring)
    elect_pipes = [mp.Pipe(duplex=True) for _ in range(N)]
    procs = []
    for i in range(N):
        p = mp.Process(target=process_node, args=(
            i, N,
            token_pipes[i][0], token_pipes[(i+1)%N][1],
            elect_pipes[i][0], elect_pipes[(i+1)%N][1],
        ))
        p.start()
        procs.append(p)

    # inject leader election start by sending node 0's id (already done by nodes themselves)
    # start token by sending it to node 0
    token_pipes[0][1].send("TOKEN")

    for p in procs:
        p.join()