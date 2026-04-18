from collections import Counter

# HashMap
# Counter
# Bucket
def frequency_sort_bucket(s: str) -> str:
    counter = Counter(s)
    max_freq = max(counter.values())
    bucket = [[] for _ in range(max_freq + 1)]
    for val, freq in counter.items():
        bucket[freq].append(val)

    res = []
    for freq in range(max_freq, 0, -1):
        for val in bucket[freq]:
            res.append(val * freq)

    return "".join(res)