from collections import defaultdict
from typing import List


# HashMap
def group_anagrams(strs: List[str]) -> List[List[str]]:
    ans = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        ans[tuple(count)].append(s)
    return list(ans.values())


def group_anagrams_sort(strs: List[str]) -> List[List[str]]:
    anagram = defaultdict(list)
    for word in strs:
        anagram[''.join(sorted(word))].append(word)
    return list(anagram.values())


print(group_anagrams_sort(['abba', 'cba', 'aba', 'aab']))