class Solution:
    def edDistRecursiveMemo(self,x, y, memo=None):
        if memo is None: memo = {}
        if len(x) == 0: return len(y)
        if len(y) == 0: return len(x)
        if (len(x), len(y)) in memo:
            return memo[(len(x), len(y))]

        delt = 1 if x[-1] != y[-1] else 0
        diag = self.edDistRecursiveMemo(x[:-1], y[:-1], memo) + delt
        vert = self.edDistRecursiveMemo(x[:-1], y, memo) + 1
        horz = self.edDistRecursiveMemo(x, y[:-1], memo) + 1
        ans = min(diag, vert, horz)
        memo[(len(x), len(y))] = ans
        return ans

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        return self.edDistRecursiveMemo(word2,word1)

if __name__== "__main__":
    s = Solution()
    print(s.minDistance("intention", "execution"))