import heapq
from collections import Counter

# HeapQ
# Counter - NLargest
# O(N*log2(K)) 我们只维护和排序一个长为k的堆，但是我们要遍历全部元素
def top_k_frequent_heap(nums, k: int):
    if k == len(nums):
        return nums
    counter = Counter(nums)
    return heapq.nlargest(k, counter.keys(), key=counter.get)


print(top_k_frequent_heap([1,1,1,2,2,3,4], 2)) #[1, 2]
print(top_k_frequent_heap([1,2,3,4], 4)) #[1, 2, 3, 4]


# O(N*log2(N)) 这里对所有进行了排序
def top_k_frequent_sort(self, nums, k: int):
    res = Counter(nums)
    return sorted(res, key=res.get, reverse=True)[:k]


# O(N) 时间复杂度是线性，但是创建了很多空桶
def top_k_frequent_bucket(nums, k: int):
    n = len(nums)
    # max freq can be n
    bucket = [[] for _ in range(n + 1)]
    counter = Counter(nums)
    for num, freq in counter.items():
        bucket[freq].append(num)
    res = []
    for freq in range(n, -1, -1):
        for num in bucket[freq]:
            res.append(num)
            if len(res) == k:
                return res
    return res