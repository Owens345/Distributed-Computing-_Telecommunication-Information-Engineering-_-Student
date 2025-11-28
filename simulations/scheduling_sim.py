#3) Scheduling Algorithms — Round-Robin vs Shortest Job First scheduler simulator
import heapq, time
from collections import deque
import random

def round_robin(jobs, m):
    # jobs: list of durations; m workers
    workers = [0]*m
    assignment = [[] for _ in range(m)]
    for i, dur in enumerate(jobs):
        w = i % m
        assignment[w].append(dur)
        workers[w] += dur
    return workers, assignment

def shortest_job_first(jobs, m):
    # greedy assign shortest job to currently least-loaded worker
    workers = [0]*m
    assignment = [[] for _ in range(m)]
    for dur in sorted(jobs):
        w = min(range(m), key=lambda x: workers[x])
        assignment[w].append(dur)
        workers[w] += dur
    return workers, assignment

if __name__ == "__main__":
    random.seed(1)
    jobs = [random.randint(1,20) for _ in range(20)]
    m = 4
    rr_workers, rr_assign = round_robin(jobs, m)
    sjf_workers, sjf_assign = shortest_job_first(jobs, m)
    print("Jobs:", jobs)
    print("RR worker loads:", rr_workers, "makespan:", max(rr_workers))
    print("SJF worker loads:", sjf_workers, "makespan:", max(sjf_workers))