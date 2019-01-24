class Solution:
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 2:
            if A[0] < A[1]:
                return 1
            elif A[0] == A[1]:
                return 1

        n = len(A)
        maxLeft = [0] * n
        minRight = [0] * n
        maxLeft[0] = A[0]
        for i in range(1, n):
            maxLeft[i] = max(A[i], maxLeft[i - 1])

        minRight[-1] = A[-1]
        for i in range(n - 2, -1, -1):
            minRight[i] = min(A[i], minRight[i + 1])

        for i in range(0, n):
            if maxLeft[i - 1] <= minRight[i]:
                return i
