class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        r = len(matrix)
        c = len(matrix[0])
        if r ==0:
            return 0
        maxlen = 0
        m = [[0] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        m[i][j] = 1
                    else:
                        m[i][j] = min(m[i - 1][j - 1], m[i - 1][j], m[i][j - 1]) + 1

                    maxlen = max(maxlen, m[i][j])

        return maxlen * maxlen


if __name__ == "__main__":
    s = Solution()
    print(s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))