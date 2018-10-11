class Solution(object):
    def backtrack(self,board,visited,r,c):
        if (r <0 or r>len(board)-1 or c<0 or c>len(board[0])-1):
            return
        if visited[r][c]==1:
            return


        if board[r][c]=="O":
            board[r][c]="1"
            self.backtrack(board, visited, r+1, c)
            self.backtrack(board, visited, r-1, c)
            self.backtrack(board, visited, r, c+1)
            self.backtrack(board, visited, r, c-1)
        visited[r][c] = 1
        return

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

        for col in range(c):
            if board[0][col]=="O":
                self.backtrack(board,visited,0,col)

            if board[r-1][col]=="O":
                self.backtrack(board,visited,r-1,col)

        for row in range(r):
            if board[row][0] == "O":
                self.backtrack(board, visited, row, 0)

            if board[row][c-1] == "O":
                self.backtrack(board, visited, row, c-1)


        #print(board)
        for i in range(r):
            for j in range(c):
                if board[i][j]=="O":
                    board[i][j]="X"

        for i in range(r):
            for j in range(c):
                if board[i][j] == "1":
                    board[i][j] = "O"

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