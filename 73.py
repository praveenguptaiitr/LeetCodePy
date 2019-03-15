class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        firstRow = 1
        firstCol = 1
        for i in range(m):
            if matrix[i][0]==0:
                firstCol=0
        for i in range(n):
            if matrix[0][i]==0:
                firstRow=0

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0] = 0

        for i in range(1,m):
            if matrix[i][0]==0:
                for j in range(1,n):
                    matrix[i][j]=0

        for j in range(1,n):
            if matrix[0][j]==0:
                for i in range(1,m):
                    matrix[i][j]=0

        if firstRow==0:
            for i in range(n):
                matrix[0][i]=0
        if firstCol==0:
            for i in range(m):
                matrix[i][0]=0

        return matrix


if __name__ == "__main__":
    s = Solution()
    print(s.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))