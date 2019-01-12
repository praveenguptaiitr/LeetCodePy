class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        n = ~0
        while n & num != 0:
            n <<= 1

        return ~n & ~num