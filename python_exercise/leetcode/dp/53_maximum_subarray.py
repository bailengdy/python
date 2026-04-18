# DP
def max_sub_array(nums) -> int:
    if not nums:
        return 0
    max_sum = nums[0]
    current_sum = 0
    for i, num in enumerate(nums):
        if current_sum < 0:
            current_sum = 0
        current_sum += num
        max_sum = max(max_sum, current_sum)
    return max_sum


