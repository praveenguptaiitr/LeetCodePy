class Solution:
    def compute(self, r, c, grid, dp):
        if r >= len(grid) or r < 0:
            return -1
        if c >= len(grid[0]) or c < 0:
            return -1

        if dp[r][c]!= 99999:
            return dp[r][c]

        l1 = self.compute(r-1,c,grid, dp)
        l2 = self.compute(r,c-1,grid, dp)
        if l1 == -1 and l2 != -1:
            dp[r][c]= grid[r][c] + l2
        if l1 != -1 and l2 == -1:
            dp[r][c]= grid[r][c] + l1
        if l1 == -1 and l2 == -1 :
            dp[r][c] = 99999
        else:
            dp[r][c]= grid[r][c] + min(l1,l2)

        return dp[r][c]

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r = len(grid)
        c = len(grid[0])
        dp = [[99999]* c for r1 in range(r)]
        #print(dp)
        dp[0][0]=grid[0][0]
        for i in range(1,len(grid[0])):
            dp[0][i]=dp[0][i-1]+ grid[0][i]
        for j in range(1,len(grid)):
            dp[j][0]=dp[j-1][0]+ grid[j][0]


        self.compute(r-1,c-1,grid,dp)
        #print(dp)
        return dp[r-1][c-1]




if __name__ == "__main__":
    s = Solution()
    print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))