from collections import deque

# Sliding Window
# Deque
class MovingAverage:

    def __init__(self, size: int):
        self.k = size
        self.current_sum = 0
        self.dq = deque()

    def next(self, val: int) -> float:
        self.dq.append(val)
        self.current_sum += val
        if len(self.dq) > self.k:
            self.current_sum -= self.dq.popleft()
        return self.current_sum / len(self.dq)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

ma = MovingAverage(2)
print(ma.next(1))
print(ma.next(2))
print(ma.next(3))
print(ma.next(4))
print(ma.next(5))