n = 5
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print(total)  # 1 + 2 + 3 + 4 + 5 = 15

# number of parameters are not fixed
def sum_all(*args):
    # args is a tuple of all positional arguments
    total = 0
    for x in args:
        total += x
    return total
print(sum_all(1, 2, 3))       # 6
print(sum_all(10, -5, 4, 1))  # 10