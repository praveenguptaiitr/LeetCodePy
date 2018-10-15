class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        n = len(A)
        if n==0:
            return -1

        if A[0]>A[1]:
            return A[0]

        if A[n-1]>A[n-2]:
            return n-1

        for i in range(1,n-2):
            if A[i]>A[i-1] and A[i]>A[i+1]:
                return i
