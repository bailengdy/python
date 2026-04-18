from collections import Counter

# HashMap
# Counter
def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


print(is_anagram("aaaab", "baaaa")) # True
print(is_anagram("aab", "baaaa")) # False
print(is_anagram("aaaab", "ccccccccc")) # False