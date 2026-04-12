# Sliding Window
# Two Pointers
def length_of_longest_substring(s: str) -> int:
    last_index = {}
    n = len(s)
    l = res = 0
    for r in range(n):
        key = s[r]
        if key in last_index:
            l = max(l, last_index[key])
        res = max(res, r - l + 1)
        last_index[key] = r + 1
    return res
