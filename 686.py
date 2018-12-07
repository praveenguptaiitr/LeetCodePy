class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if len(A) == 1 and len(B) == 1 and A != B:
            return -1

        if B in A:
            return 1
        i = 2
        while (True):
            s = A * i
            if len(s) > 10000:
                return -1
            elif B in s:
                return i
            else:
                i += 1
        return -1
