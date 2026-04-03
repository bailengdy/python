# Solution 1
def even_squares(nums):
    return [x * x for x in nums if x % 2 == 0]

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(even_squares(nums))

# Solution 2
nums = [1, 2, 3, 4, 5, 6]
squares = []
for x in nums:
    if x % 2 == 0:
        squares.append(x * x)
print(squares)  # [4, 16, 36]