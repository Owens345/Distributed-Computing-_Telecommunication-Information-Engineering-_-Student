#8. LARGE SCALE DATA PROCESSING ALGORITHMS (MapReduce)
from collections import defaultdict

def map_phase(text):
    """Perform the map phase by splitting text into words and emitting (word,1) pairs."""
    words = text.split()
    mapped = []
    for w in words:
        # Convert word to lowercase to normalize
        mapped.append((w.lower(), 1))
    return mapped

def reduce_phase(mapped_pairs):
    """Reduce phase: aggregate counts for each word emitted by the map phase."""
    result = defaultdict(int)
    for word, count in mapped_pairs:
        result[word] += count
    return result

def demo_mapreduce():
    """Demonstrate MapReduce by performing word counting on sample text."""
    text = "MapReduce is great and MapReduce is powerful"
    mapped = map_phase(text)
    reduced = reduce_phase(mapped)
    print("MapReduce Demonstration:")
    print("Mapped Output:", mapped)
    print("Reduced Output:", dict(reduced))