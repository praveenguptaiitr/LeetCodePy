class Solution(object):
    def checkBox(self, board,r,c,v):
        r1 = (int(r/3))*3
        c1 = (int(c/3))*3
        count=0
        for i in range(3):
            for j in range(3):
                if board[r1+i][c1+j]==v and r1+i != r and c1+j!=c:
                    return False
        return True

    def checkValid(self, board, d):
        r = int(d/9)
        c = d%9
        v = board[r][c]
        count=0
        for i in range(0,9):
            if board[i][c]==v and i!=r:
                return False
            if board[r][i]==v and i!=c:
                return False

        if self.checkBox(board,r,c, v):
            return True
        else:
            return False

    def place(self, board, d):
        if d == 81:
            return True
        else:
            r = int(d/9)
            c = d%9
            if board[r][c]==".":
                return self.place(board, d+1)
            else:
                if self.checkValid(board, d):
                    return self.place(board,d+1)
                else:
                    return False

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return self.place(board,0)


if __name__ == "__main__":
    s = Solution()
    print(s.isValidSudoku([["5","3",".",".","7",".",".",".","."],
                     ["6",".",".","1","9","5",".",".","."],
                     [".","9","8",".",".",".",".","6","."],
                     ["8",".",".",".","6",".",".",".","3"],
                     ["4",".",".","8",".","3",".",".","1"],
                     ["7",".",".",".","2",".",".",".","6"],
                     [".","6",".",".",".",".","2","8","."],
                     [".",".",".","4","1","9",".",".","5"],
                     [".",".",".",".","8",".",".","7","9"]]))
