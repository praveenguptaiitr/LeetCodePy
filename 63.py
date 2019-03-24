class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0]==1:
            return 0

        r = len(obstacleGrid)
        c = len(obstacleGrid[0])

        tbl = [[0]*c for i in range(r)]
        tbl[0][0]=1
        for i in range(1,r):
            if obstacleGrid[i][0]==1:
                tbl[i][0]=0
            else:
                tbl[i][0]= tbl[i-1][0]

        for j in range(1,c):
            if obstacleGrid[0][j]==1:
                tbl[0][j]=0
            else:
                tbl[0][j]= tbl[0][j-1]

        for i in range(1,r):
            for j in range(1,c):
                if obstacleGrid[i][j]==1:
                    tbl[i][j]=0
                else:
                    tbl[i][j]=tbl[i-1][j]+tbl[i][j-1]

        return tbl[r-1][c-1]


if __name__ == "__main__":
    s = Solution()
    print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
