# Sliding Window
# Two Pointers
def min_sub_array_len(target: int, nums) -> int:
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