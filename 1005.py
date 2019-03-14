import heapq


class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if len(A) == 0:
            return
        if K == 0:
            return sum(A)

        heapq.heapify(A)
        for i in range(K):
            a = heapq.heappop(A)
            a = a * (-1)
            heapq.heappush(A, a)

        return sum(A)
