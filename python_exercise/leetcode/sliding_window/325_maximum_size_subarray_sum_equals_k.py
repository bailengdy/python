# Sliding Window
# Prefix Sum + HashMap(First seen Index)
def max_sub_array_len(nums, k) -> int:
    indices = {0: -1}
    pSum = res = 0
    for i, num in enumerate(nums):
        pSum += num
        if pSum - k in indices:
            res = max(res, i - indices[pSum - k])
        if pSum not in indices:
            indices[pSum] = i
    return res