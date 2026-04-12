# Sliding Window
# Sort
def max_frequency(nums, k: int) -> int:
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


print(max_frequency([1,2,3,4], 3)) # 3
print(max_frequency([1,2,3,4], 6)) # 4
print(max_frequency([1,2,3,4], 5)) # 3
print(max_frequency([1], 0)) # 1
print(max_frequency([1, 1, 1, 1], 0)) # 4
print(max_frequency([3, 9, 6], 2)) # 1
print(max_frequency([9930,9923,9983,9997,9934,9952,9945,9914,9985,9982,9970,9932,9985,9902,9975,9990,9922,9990,9994,9937,9996,9964,9943,9963,9911,9925,9935,9945,9933,9916,9930,9938,10000,9916,9911,9959,9957,9907,9913,9916,9993,9930,9975,9924,9988,9923,9910,9925,9977,9981,9927,9930,9927,9925,9923,9904,9928,9928,9986,9903,9985,9954,9938,9911,9952,9974,9926,9920,9972,9983,9973,9917,9995,9973,9977,9947,9936,9975,9954,9932,9964,9972,9935,9946,9966], 3056)) # 73