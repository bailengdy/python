# Sliding Window
# Two Pointers
def longest_ones(nums, k: int) -> int:
    res = l = count_zero = 0
    for r, num in enumerate(nums):
        if num == 0:
            count_zero += 1
        while count_zero > k:
            if nums[l] == 0:
                count_zero -= 1
            l += 1
        res = max(res, r - l + 1)
    return res


print(longest_ones([1,1,1,0,0,1,1], 2)) #7
print(longest_ones([1,1,1,0,0,1,1], 1)) #4