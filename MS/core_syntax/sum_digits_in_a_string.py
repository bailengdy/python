s = "a1b2c3d4"
total = 0

for ch in s:
    if ch.isdigit():          # 如果是数字字符 / if it's a digit
        total += int(ch)

print(total)  # 1 + 2 + 3 + 4 = 10