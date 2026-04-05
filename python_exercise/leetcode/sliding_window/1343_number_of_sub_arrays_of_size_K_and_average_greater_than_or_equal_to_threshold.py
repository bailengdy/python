# Sliding Window
# Maintain a metric
def num_of_subarrays(arr, k: int, threshold: int) -> int:
    res = s = 0
    for i in range(k):
        s += arr[i]
    if s / k >= threshold:
        res += 1
    for i in range(k, len(arr)):
        s -= arr[i - k]
        s += arr[i]
        if s / k >= threshold:
            res += 1
    return res


def num_of_subarrays_optimised(arr, k: int, threshold: int) -> int:
    s = 0
    target_sum = threshold * k
    s = sum(arr[:k])
    res = 1 if s >= target_sum else 0
    for i in range(k, len(arr)):
        s = s - arr[i - k] + arr[i]
        if s >= target_sum:
            res += 1
    return res