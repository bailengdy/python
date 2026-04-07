from collections import Counter

# HeapQ
# Counter - most_common
def f(nums, k): return [x for x, _ in Counter(nums).most_common(k)]
