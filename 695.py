class Solution(object):
    def visit(self, grid, visited, i,j):
        if(i<0 or j<0 or i>=len(grid)or j>= len(grid[0])):
            return 0

        if visited[i][j]==1:
            return 0

        visited[i][j]=1
        if grid[i][j]==1:
            return 1 + self.visit(grid,visited,i+1,j) + self.visit(grid,visited,i-1,j)+self.visit(grid,visited,i,j+1)+self.visit(grid,visited,i,j-1)

        return 0


    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if (len(grid))==0:
            return 0

        r = len(grid)
        c = len(grid[0])
        visited = [[0]*c for i in range(r)]
        m = 0

        for i in range(r):
            for j in range(c):
                if grid[i][j]==1 and visited[i][j]!=1:
                    ans = self.visit(grid,visited,i,j)
                    if ans > m:
                        m = ans

        return m

if __name__=="__main__":
    s = Solution()
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(s.maxAreaOfIsland(grid))