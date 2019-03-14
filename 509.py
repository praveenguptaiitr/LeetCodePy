class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 1:
            return N
        a = 0
        b = 1
        c = 1
        for i in range(2, N + 1):
            a = b
            b = c
            c = a + b
        return b


