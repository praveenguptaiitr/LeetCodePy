class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        for i in range(r):
            for j in range(i+1,c):
                matrix[i][j], matrix[j][i]=matrix[j][i],matrix[i][j]

        #print(matrix)
        for i in range(r):
            for j in range(c//2):
                t = matrix[i][j]
                matrix[i][j] = matrix[i][c-j-1]
                matrix[i][c - j-1] = t


        #return matrix



if __name__ == "__main__":
    s = Solution()
    mat = [
        [ 1,2,3],
        [ 4,5,6],
        [7,8,9]
        ]

    print(s.rotate(mat))