class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0 or n == 1:
            return 1

        g = [0]*(n+1)
        g[0]=1
        g[1]=1

        for i in range(2,n+1):
            for j in range(1,i+1):
                g[i]+=g[j-1]*g[i-j]

        return g[n]