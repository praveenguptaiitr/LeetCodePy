class Solution(object):
    def backtrack(self,board,visited,r,c):
        if r <0 or r>=len(board) or c<0 or c>=len(board[0]):
            return True

        if (r==0 or r==(len(board)-1) or c==0 or c==(len(board[0])-1)):
                visited[r][c] = 1
                return False

        if visited[r][c]==1:
            return True

        visited[r][c] = 1
        ans1 = self.backtrack(board,visited,r-1,c)
        ans2 = self.backtrack(board,visited,r+1,c)
        ans3 = self.backtrack(board,visited,r,c-1)
        ans4 = self.backtrack(board,visited,r,c+1)
        if (ans1 and ans2 and ans3 and ans4) and (board[r][c]=="O"):
            board[r][c]="X"
            #visited[r][c] = 1
            return True


        return True

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board)==0:
            return

        visited = [[0]*len(board[0]) for i in range(len(board))]
        r = len(board)
        c = len(board[0])

        for i in range(r):
            for j in range(c):
                if (board[i][j]=="X"):
                    visited[i][j]=1
                if(board[i][j]=="O" and visited[i][j]!=1):
                    self.backtrack(board,visited,i,j)

        return

if __name__== "__main__":
    board = [["X","O","X","O","X","O"],
             ["O","X","O","X","O","X"],
             ["X","O","X","O","X","O"],
             ["O","X","O","X","O","X"]]

    print(board)
    s = Solution()
    s.solve(board)
    print(board)