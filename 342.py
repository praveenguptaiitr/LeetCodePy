class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        if num == 1:
            return True

        for i in range(0, 33, 2):
            if 1 << i == num:
                return True

        return False