def avg(nums):
    if not nums:
        return 0.0
    return sum(nums) / len(nums)

print(avg([1, 2, 3]))  # 2.0