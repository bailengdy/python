import heapq

# HeapQ
class KthLargest:

    def __init__(self, k: int, nums):
        self.min_heap = []
        self.k = k
        for val in nums:
            self.add(val)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k or self.min_heap[0] < val:
            heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]


kl = KthLargest(3, [1, 2])
print(kl.add(3))  # 1
print(kl.add(4))  # 2
print(kl.add(5))  # 3
print(kl.add(0))  # 3