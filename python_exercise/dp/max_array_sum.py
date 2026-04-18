def max_subset_sum(arr):
    prev, curr = 0, 0
    for x in arr:
        prev, curr = curr, max(curr, prev + x)
    return curr