# Sliding Window
def count_greater(nums, k, threshold):
    count = 0
    res = []
    # 初始化窗口
    for i in range(k):
        if nums[i] > threshold:
            count += 1
    res.append(count)

    # 滑动窗口
    for i in range(k, len(nums)):
        # 移出
        if nums[i - k] > threshold:
            count -= 1
        # 加入
        if nums[i] > threshold:
            count += 1
        res.append(count)

    return res
