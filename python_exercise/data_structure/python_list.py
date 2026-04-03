nums = [10, 20, 30, 40, 50]

# 随机访问 / random access: O(1)
first = nums[0]     # 10
third = nums[2]     # 30
last = nums[-1]     # 50

# 尾部插入 / append at tail: 摊销 O(1)
nums.append(60)
nums.append(70)

print(nums)  # [10, 20, 30, 40, 50, 60, 70]

# 随机访问：nums[i]是O(1)，因为底层是连续内存 + index计算。
# 尾部插入append：扩容时有occasionallyO(n)，但摊销下来是O(1)。


nums = [10, 20, 30, 40, 50]

# 在开头插入一个元素 / insert at head: O(n)
nums.insert(0, 5)

print(nums)  # [5, 10, 20, 30, 40, 50]

# Insert at the beginning of a dynamic array is O(n),
# because all existing elements have to be shifted by one position.