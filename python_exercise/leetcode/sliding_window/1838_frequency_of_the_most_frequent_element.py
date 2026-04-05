# Sliding Window
# Sort
def max_frequency(self, nums, k: int) -> int:
    nums.sort()
    current_sum = l = res = 0
    for r, num in enumerate(nums):
        target = num
        current_sum += target
        while (r - l + 1) * target - current_sum > k:
            current_sum -= nums[l]
            l += 1
        res = max(res, r - l + 1)
    return res
