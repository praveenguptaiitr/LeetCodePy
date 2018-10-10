class Solution(object):
    def visit(self,grid, visited,i,j):
        if(i<0 or i>=len(grid)):
            return
        if(j<0 or j >=len(grid[0])):
            return
        if(visited[i][j]==1):
            return
        if(grid[i][j]=="1"):
            visited[i][j]=1
            self.visit(grid,visited,i+1,j)
            self.visit(grid, visited, i-1, j)
            self.visit(grid, visited, i, j-1)
            self.visit(grid, visited, i, j+1)

        return

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid)==0:
            return 0

        total = 0
        c = len(grid[0])
        r = len(grid)
        #visited = [[0]*c]*r
        visited = [[0] * c for i in range(r)]
        for i in range(0,r):
            for j in range(0,c):
                if(grid[i][j]=="1" and visited[i][j]!=1):
                    total+=1
                    self.visit(grid,visited,i,j)

        return total


if __name__=='__main__':
    grid = [["0","1","0"],["1","0","1"],["0","1","0"]]
    s = Solution()
    print(s.numIslands(grid))