# Sliding Window
# Prefix Sum + HashMap(Count)
def subarray_sum(nums, k: int) -> int:
    indices = {0: 1}
    p_sum = res = 0
    for i, num in enumerate(nums):
        p_sum += num
        if p_sum - k in indices:
            res += indices[p_sum - k]
        indices[p_sum] = indices.get(p_sum, 0) + 1
    return res


print(subarray_sum([1,1,1,1], 2)) #3
print(subarray_sum([1,-1,1,-1], 0)) #4
print(subarray_sum([], 0)) #0