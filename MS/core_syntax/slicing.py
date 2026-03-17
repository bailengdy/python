arr = [0, 1, 2, 3, 4, 5, 6]

print(arr[1:4])   # [1, 2, 3]  from index 1 to 3
print(arr[:3])    # [0, 1, 2]  from start to 2
print(arr[4:])    # [4, 5, 6]  from 4 to end
print(arr[::2])   # [0, 2, 4, 6] step = 2
print(arr[::-1])  # [6, 5, 4, 3, 2, 1, 0] reversed