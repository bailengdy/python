def f(nums, k):
    l = s = 0
    res = 0
    for r in range(len(nums)):
        s += nums[r]
        while s > k:
            s -= nums[l]
            l += 1
        res = max(res, r - l + 1)
    return res
