from collections import Counter

# HashMap
# Counter
def first_uniq_har(self, s: str) -> int:
    counter = Counter(s)
    for i, c in enumerate(s):
        if counter[c] == 1:
            return i
    return -1


print(first_uniq_har("leetcode")) #0
print(first_uniq_har("bbbbbaaaai")) #9
print(first_uniq_har("aabb")) #-1