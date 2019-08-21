import heapq


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.first = []
        self.second = []
        self.n = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if self.n == 0:
            heapq.heappush(self.first, -1 * num)
            self.n = 1
            return
        if num > -1 * (self.first[0]):
            heapq.heappush(self.second, num)
        else:
            heapq.heappush(self.first, -1 * num)

        if len(self.first) > len(self.second):
            if len(self.first) - len(self.second) > 1:
                x = heapq.heappop(self.first) * -1
                heapq.heappush(self.second, x)

        elif len(self.second) > len(self.first):
            if len(self.second) - len(self.first) > 1:
                x = heapq.heappop(self.second)
                heapq.heappush(self.first, x * -1)

        self.n = len(self.first) + len(self.second)
        return

    def findMedian(self):
        """
        :rtype: float
        """
        if self.n % 2 == 0:
            return ((self.first[0] * -1.0) + (self.second[0])) / 2
        else:
            if len(self.first) > len(self.second):
                return self.first[0] * -1

        return self.second[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

if __name__ == "__main__":
    s = MedianFinder()
    s.addNum(1)
    s.addNum(2)
    print(s.findMedian())
