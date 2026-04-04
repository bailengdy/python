# Sliding Window
# Prefix Sum + HashMap(Count)
def subarray_sum(self, nums: List[int], k: int) -> int:
    indices = {0: 1}
    pSum = res = 0
    for i, num in enumerate(nums):
        pSum += num
        if pSum - k in indices:
            res += indices[pSum - k]
        indices[pSum] = indices.get(pSum, 0) + 1
    return res