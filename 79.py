class Solution:

    def dfs(self, board, word,k, i, j, visited):
        if i < 0 or i >= len(board):
            return False
        if j < 0 or j>= len(board[0]):
            return False

        if visited[i][j]!=1:

            if word[k]==board[i][j]:
                if k==len(word)-1:
                    return True
                else:
                    v = visited[:]
                    v[i][j]=1

                    a1 =  self.dfs(board, word, k+1,i+1,j, v) \
                        or self.dfs(board, word, k+1,i-1,j, v) \
                        or self.dfs(board, word, k+1,i,j+1, v) \
                        or self.dfs(board, word, k+1,i,j-1, v)
                    if a1 == True:
                        return True
                    else:
                        v[i][j]=0
                        return False
            else:
                return False
        else:
            return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        r = len(board)
        c = len(board[0])

        #visited = [[0]*c for i in range(r)]
        ans = False
        for i in range(r):
            for j in range(c):
                if word[0]==board[i][j]:
                    visited = [[0] * c for i in range(r)]
                    a1 = self.dfs(board, word, 0, i , j, visited)
                    ans = ans or a1

        return ans



if __name__ == "__main__":
    s = Solution()
    board = [
                ["A","B","C","E"],
                ["S","F","E","S"],
                ["A","D","E","E"]
             ]

    word = "ABCESEEEFS"
    print(s.exist(board, word))