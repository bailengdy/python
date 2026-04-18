# Sliding Window
# Prefix Sum
class NumArray:

    def __init__(self, nums):
        self.prefix = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            self.prefix[i + 1] = self.prefix[i] + num

    def sum_range(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


na = NumArray([1,2,3,4,5,6])
print(na.sum_range(0, 3)) #10
print(na.sum_range(1, 5)) #20