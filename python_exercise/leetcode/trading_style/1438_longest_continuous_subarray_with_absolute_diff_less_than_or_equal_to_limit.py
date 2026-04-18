from collections import deque

# Sliding Window
# 2 Deque
def longest_subarray(nums, limit: int) -> int:
    min_dq = deque()
    max_dq = deque()
    res = l = 0
    for r, num in enumerate(nums):
        # print("-----------------")
        # print(f"Process value: {num}")
        while min_dq and min_dq[-1] > num:
            min_dq.pop()
        while max_dq and max_dq[-1] < num:
            max_dq.pop()
        max_dq.append(num)
        min_dq.append(num)
        # print(min_dq)
        # print(max_dq)
        while max_dq[0] - min_dq[0] > limit:
            if max_dq[0] == nums[l]:
                max_dq.popleft()
            if min_dq[0] == nums[l]:
                min_dq.popleft()
            l += 1
        res = max(res, r - l + 1)
    return res


print(longest_subarray([1,2,3,3,3,4,5], 0)) #3
print(longest_subarray([9,2,3,3,3,4,5], 2)) #5
print(longest_subarray([9,2,3,6,3,4,5], 2)) #3