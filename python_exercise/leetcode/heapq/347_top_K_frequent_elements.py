import heapq
from collections import Counter

# HeapQ
# Counter - NLargest
def top_k_frequent(nums, k: int) -> List[int]:
    if k == len(nums):
        return nums
    counter = Counter(nums)
    return heapq.nlargest(k, counter.keys(), key=counter.get)