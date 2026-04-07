import heapq

# HeapQ * 2
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def add_num(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))

        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def find_median(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2


class MedianFinderOptimised:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def add_num(self, num: int) -> None:
        if len(self.minheap) == len(self.maxheap):
            heapq.heappush(self.maxheap, -(heapq.heappushpop(self.minheap, num)))
        else:
            heapq.heappush(self.minheap, -(heapq.heappushpop(self.maxheap, -num)))

    def find_median(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return float((self.minheap[0] - self.maxheap[0]) / 2)
        else:
            return float(-self.maxheap[0])

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()