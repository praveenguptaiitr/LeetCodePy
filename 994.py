class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid)==1 and len(grid[0])==1:
            if grid[0][0]==0 or grid[0][0]==2:
                return 0
            else:
                return -1
        rotten = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    rotten.append((i,j))


        q = []
        for i in range(len(rotten)):
            q.append(rotten[i])
        time = -1
        row = len(grid)
        col = len(grid[0])
        visited = [[0]*col for i in range(row)]

        while(len(q)>0):
            time+=1
            next = []
            while(len(q)>0):
                x,y = q.pop()
                visited[x][y]=1
                if grid[x][y]==1:
                    grid[x][y]=2
                # x-1,y
                # x+1,y
                # x,y-1
                # x,y+1

                if (x-1)>=0 and visited[x-1][y]==0 and grid[x-1][y]==1:
                    next.append((x-1,y))
                    grid[x - 1][y]=2
                if x+1< row and visited[x+1][y]==0 and grid[x+1][y]==1:
                    next.append((x+1,y))
                    grid[x + 1][y]=2
                if y-1>=0 and visited[x][y-1]==0 and grid[x][y-1]==1:
                    next.append((x,y-1))
                    grid[x][y - 1]=2

                if y+1< col and visited[x][y+1]==0 and grid[x][y+1]==1:
                    next.append((x,y+1))
                    grid[x][y + 1]=2
            if (len(next)==0):
                break
            q = next
            next=[]


        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    return -1

        return time

if __name__ == "__main__":
    s = Solution()
    print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
    print(s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
    print(s.orangesRotting([[0,2]]))
    print(s.orangesRotting([[0]]))
    print(s.orangesRotting([[1]]))
    print(s.orangesRotting([[2]]))
    print(s.orangesRotting([[2,2],[1,1],[0,0],[2,0]]))