class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        l = []
        rend = len(matrix) - 1
        cend = len(matrix[0]) - 1
        rs = 0
        cs = 0
        count = (rend + 1) * (cend + 1)
        dy = [1, 0, -1, 0]
        dx = [0, 1, 0, -1]
        l.append(matrix[0][0])
        turn = 0
        x = 0
        y = 0
        while (count > 1):

            tx = dx[turn]
            ty = dy[turn]
            while (x + tx <= rend and x + tx >= rs and y + ty <= cend and y + ty >= cs):
                count -= 1
                l.append(matrix[x + tx][y + ty])
                x += tx
                y += ty

            if turn == 0:
                rs += 1
            if turn == 1:
                cend -= 1
            if turn == 2:
                rend -= 1
            if turn == 3:
                cs += 1
            turn += 1
            turn = turn % 4

        return l


if __name__ == "__main__":
    g = [[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]
    s = Solution()
    print(s.spiralOrder(g))
