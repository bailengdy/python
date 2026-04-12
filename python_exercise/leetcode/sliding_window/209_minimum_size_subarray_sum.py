# Sliding Window
# Two Pointers
def min_sub_array_len(nums, target) -> int:
    n = len(nums)
    l = s = 0
    res = n + 1
    for r in range(n):
        s += nums[r]
        while s >= target:
            res = min(res, r - l + 1)
            s -= nums[l]
            l += 1
    return 0 if res == n + 1 else res


print(min_sub_array_len([1, 1], 2)) # 2
print(min_sub_array_len([1, 1, 1], 2)) # 2
print(min_sub_array_len([1, 2, 1], 2)) # 1
print(min_sub_array_len([1, 1, 1], 5)) # 0
print(min_sub_array_len([1, 2, 3, 4, 5], 15)) # 0