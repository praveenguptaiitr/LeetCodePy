class Solution(object):
    def __init__(self):
        self.d = 0

    def check_block(self, board, r,c,x):
        r1 = (int(r/3))*3
        c1 = (int(c/3))*3
        canAdd = True
        for i in range(3):
            for j in range(3):
                if board[r1+i][c1+j]==str(x):
                    return False

        return True

    def construct_candidates(self,board, d):
        candidates = []
        r = int(d/9)
        c = d%9
        for x in range(1,10):
            canAdd = True
            for i in range(0,9):
                if board[r][i]==str(x) or board[i][c]==str(x):
                    canAdd=False
            if canAdd==True:
                candidates.append(x)
        ans = []
        for c1 in candidates:
            if self.check_block(board, r, c, c1)==True:
                ans.append(c1)
        ans = [str(a) for a in ans]
        return ans

    def place(self, board, d):
        if d == 81:
            #print(board)
            return True
        i = int(d/9)
        j = d%9
        if board[i][j]!= ".":
            return self.place(board,d+1)
        else:
            can = self.construct_candidates(board,d)
            for x in can:
                board[i][j]= x
                if self.place(board,d+1):
                    return True
                else:
                    board[i][j]="."
        return False

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        self.place(board, 0)
        #print(board)

if __name__ == "__main__":
    s = Solution()
    print(s.solveSudoku([["5","3",".",".","7",".",".",".","."],
                   ["6",".",".","1","9","5",".",".","."],
                   [".","9","8",".",".",".",".","6","."],
                   ["8",".",".",".","6",".",".",".","3"],
                   ["4",".",".","8",".","3",".",".","1"],
                   ["7",".",".",".","2",".",".",".","6"],
                   [".","6",".",".",".",".","2","8","."],
                   [".",".",".","4","1","9",".",".","5"],
                   [".",".",".",".","8",".",".","7","9"]]))