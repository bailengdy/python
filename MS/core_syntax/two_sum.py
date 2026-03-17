def two_sum(nums, target):
    index = {}
    for i, x in enumerate(nums):
        y = target - x
        if y in index:
            return index[y], i
        index[x] = i
    return None
