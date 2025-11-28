#7) Data Partitioning & Sharding — Hash partitioning vs Range partitioning demo
import hashlib

def hash_shard(key, num_shards):
    h = int(hashlib.md5(str(key).encode()).hexdigest(),16)
    return h % num_shards

def range_shard(key, boundaries):
    # boundaries: sorted list of max keys per shard
    for i, b in enumerate(boundaries):
        if key <= b:
            return i
    return len(boundaries)

if __name__ == "__main__":
    keys = [3, 27, 101, 250, 999]
    num_shards = 3
    print("Hash partitioning routing:")
    for k in keys:
        print(k, "-> shard", hash_shard(k, num_shards))

    print("\nRange partitioning routing (boundaries [100,500]):")
    boundaries = [100, 500]
    for k in keys:
        print(k, "-> shard", range_shard(k, boundaries))