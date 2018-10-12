class Solution(object):
    def generateMatrix(self, n):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if n==0 :
            return [[]]
        elif n==1:
            return [[1]]

        else:
            rend = n - 1
            cend = n - 1
            rs = 0
            cs = 0
            count = 1
            matrix = [[0]*n for i in range(n)]
            dy = [1, 0, -1, 0]
            dx = [0, 1, 0, -1]
            matrix[0][0]=count
            turn = 0
            x = 0
            y = 0
            sqr = n*n
            while (count < sqr):

                tx = dx[turn]
                ty = dy[turn]
                while (x + tx <= rend and x + tx >= rs and y + ty <= cend and y + ty >= cs):
                    count += 1
                    x += tx
                    y += ty
                    matrix[x][y]=count

                if turn == 0:
                    rs += 1
                elif turn == 1:
                    cend -= 1
                elif turn == 2:
                    rend -= 1
                else:
                    cs += 1
                turn += 1
                turn %= 4

            return matrix


if __name__ == "__main__":
    #g = [[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]
    s = Solution()
    n=3
    print(s.generateMatrix(n))
