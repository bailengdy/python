from collections import Counter

# HashMap
# Counter
# Sort
def top_k_frequent_sort(self, words, k: int):
    counter = Counter(words)
    return sorted(counter.keys(), key=lambda x: (-counter[x], x))[:k]
