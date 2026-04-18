from collections import defaultdict
from typing import List

# HahMap
# Strings
# List Comprehensions
def find_duplicate(paths: List[str]) -> List[List[str]]:
    duplicates = defaultdict(list)
    for path in paths:
        parts = path.split()
        d = parts[0]
        for file in parts[1:]:
            i1 = file.index('(')
            i2 = file.index(')')
            filename = f"{d}/{file[:i1]}"
            content = file[i1 + 1:i2]
            duplicates[content].append(filename)
    return [files for _, files in duplicates.items() if len(files) > 1]