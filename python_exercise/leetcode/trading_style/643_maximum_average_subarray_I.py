# Sliding Window
# Slicing
def find_max_average(nums, k: int) -> float:
    current_sum = sum(nums[:k])
    max_sum = current_sum
    for i in range(k, len(nums)):
        current_sum -= nums[i - k]
        current_sum += nums[i]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum / k

#####################################################
# We maintain a running sum over the window.
# When the window moves, we update the sum in O(1)
# by adding the new element and removing the old one.

print(find_max_average([1,2,3,4,5], 3))