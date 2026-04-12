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
        self.first = []
        self.second = []

    def add_num(self, val: int) -> None:
        if len(self.first) == len(self.second):
            heapq.heappush(self.first, -heapq.heappushpop(self.second, val))
        else:
            heapq.heappush(self.second, -heapq.heappushpop(self.first, -val))

    def find_median(self) -> float:
        if len(self.first) > len(self.second):
            return -self.first[0]
        return (-self.first[0] + self.second[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

mf = MedianFinder()
mf.add_num(1)
print(mf.find_median())
mf.add_num(9)
print(mf.find_median())
mf.add_num(7)
# print(mf.first)
# print(mf.second)
print(mf.find_median())
