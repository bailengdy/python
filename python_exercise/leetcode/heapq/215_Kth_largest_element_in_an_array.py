import heapq

# HeapQ
# Sort
def find_kth_largest_optimised(nums, k: int) -> int:
    nums.sort(reverse=True)
    return nums[k - 1]


def find_kth_largest(nums, k: int) -> int:
    return heapq.nlargest(k, nums)[-1]