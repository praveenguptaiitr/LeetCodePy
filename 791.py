class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """

        d = {}
        for idx, v in enumerate(S):
            d[v]=idx

        for i in T:
            if d.get(i,-1)==-1:
                d[i]=float("Inf")

        #print(str(d))
        ans = sorted(T, key = lambda x : d[x])
        return "".join(ans)
        #print(T)


if __name__ == "__main__":
    s = Solution()
    s.customSortString("cba", "abcd")