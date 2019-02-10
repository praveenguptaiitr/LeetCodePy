import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = heapq.nlargest(k, nums)
        heapq.heapify(self.heap)
        #self.k_list = heapq.nlargest(k, nums)


    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.heap)<self.k:
            heapq.heappush(self.heap,val)
        else:
            if val > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, val)

        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)