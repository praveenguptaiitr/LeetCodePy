class Solution(object):

    def search(self, matrix, rl,rh,cl,ch, target):

        if rl > rh or cl>ch:
            return False

        if rl < 0 or cl < 0 or rh > len(matrix) or ch> len(matrix[0]):
            return False

        if rl == rh and cl == ch:
            if matrix[rl][cl]==target:
                return True
            else:
                return False

        if matrix[rl][cl]==target or matrix[rh][ch]==target:
            return True

        midr = (rl+rh)//2
        midc = (cl+ch)//2

        if matrix[midr][midc]==target:
            return True
        elif matrix[midr][midc] > target:
            return ( self.search(matrix, rl,midr,cl,midc, target)
                    or self.search(matrix, midr+1, rh, cl, midc, target)
                    or self.search(matrix, rl, midr , midc+1, ch, target) )

        else:
            return ( self.search(matrix,midr+1, rh,midc+1,ch, target)
                    or self.search(matrix, midr+1, rh, cl, midc, target)
                    or self.search(matrix, rl, midr , midc+1, ch, target) )




    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        r = len(matrix)
        if r == 0 :
            return False
        c = len(matrix[0])
        if c == 0:
            return False

        if r==1 and c==1:
            if matrix[0][0]==target:
                return True
            else:
                return False

        return self.search(matrix, 0, r-1, 0, c-1, target)
