# Sliding Window
# HeapQ
from collections import deque


def min_sliding_window(nums, k):
    dq, res = deque(), []
    for i in range(len(nums)):
        num = nums[i]
        if dq and dq[0] < i - k + 1: dq.popleft()
        while dq and nums[dq[-1]] > num: dq.pop()
        dq.append(i)
        if i >= k - 1: res.append(nums[dq[0]])
    return res


print(min_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))
#[-1, -3, -3, -3, 3, 3]