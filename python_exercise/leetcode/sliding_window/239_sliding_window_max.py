# Sliding Window
# HeapQ
from collections import deque


def max_sliding_window(self, nums: List[int], k: int) -> List[int]:
    dq, res = deque(), []
    for i in range(len(nums)):
        num = nums[i]
        if dq and dq[0] < i - k + 1: dq.popleft()
        while dq and nums[dq[-1]] < num: dq.pop()
        dq.append(i)
        if i >= k - 1: res.append(nums[dq[0]])
    return res


def max_sliding_window_optimised(self, nums: List[int], k: int) -> List[int]:
    dq = deque()
    res = []

    for i in range(k):
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()
        dq.append(i)

    res.append(nums[dq[0]])

    for i in range(k, len(nums)):
        if dq and dq[0] == i - k:
            dq.popleft()
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()

        dq.append(i)
        res.append(nums[dq[0]])

    return res


print(max_sliding_window([1,2,3,4], 3)) #[3, 4]
print(max_sliding_window([1], 1)) #[1]
print(max_sliding_window([1, -1], 1)) #[1, -1]