class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        if len(matrix)==0 or len(matrix[0])==0:
            self.mat=[]
            return
        if len(matrix)==1 and len(matrix[0])==1:
            a = matrix[0][0]
            self.mat =[[a]]
            return
        #self.matrix = matrix
        self.mat = [[0]*len(matrix[0]) for i in matrix]
        self.mat[0][0]= matrix[0][0]
        for i in range(1, len(matrix[0])):
            self.mat[0][i]= self.mat[0][i-1]+ matrix[0][i]
        for i in range(1, len(matrix)):
            self.mat[i][0]= self.mat[i-1][0]+ matrix[i][0]

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                self.mat[i][j]= self.mat[i-1][j]+ self.mat[i][j-1]-self.mat[i-1][j-1]+ matrix[i][j]




    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1 == row2 and col1 == col2:
            return self.matrix[row1][col1]

        if row1 == 0 and col1 == 0:
            return self.mat[row2][col2]

        if row1 ==0 and col1!=0:
            return (self.mat[row2][col2] - self.mat[row2][col1 - 1])
        if row1!=0 and col1==0:
            return (self.mat[row2][col2]  - self.mat[row1 - 1][col2])

        if 0 <row1<=row2 < len(self.mat) and 0 < col1<=col2 < len(self.mat[0]):
            return (self.mat[row2][col2] + self.mat[row1-1][col1-1] - self.mat[row1-1][col2] - self.mat[row2][col1-1])

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
