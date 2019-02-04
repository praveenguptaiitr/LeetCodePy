import heapq
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for i in range(k):
            heap.append(nums[i])

        heapq.heapify(heap)
        for i in range(k,len(nums)):
            if nums[i]>heap[0]:
                    heapq.heapreplace(heap,nums[i])

        return heap[0]


if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargest([2,1],1))