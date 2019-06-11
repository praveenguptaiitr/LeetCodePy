class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return self.myPow(1 / x, -1*n)
        else:
            v = self.myPow(x, n // 2)
            return v * v * (x if n % 2 != 0 else 1)


if __name__ == "__main__":
    s = Solution()
    print(s.myPow(2.000, -2))