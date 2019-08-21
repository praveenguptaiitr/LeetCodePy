from collections import Counter

class Solution(object):
    def __init__(self):
        self.dict = {}

    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """

        strs.insert(0,"")
        tbl = [ [[0]* (n+1) for _ in range(m+1)] for _ in range(len(strs))]

        m1 = [0]*(len(strs)+1)
        n1 = [0]*(len(strs)+1)

        for i in range(len(strs)):
            c = Counter(strs[i])
            m1[i]=c["0"]
            n1[i] = c["1"]

        for i in range(1,len(strs)):
            for j in range(m+1):
                for k in range(n+1):
                    if j>=m1[i] and k >= n1[i]:
                        tbl[i][j][k]=max(tbl[i-1][j][k],tbl[i-1][j-m1[i]][k-n1[i]]+1)
                    else:
                        tbl[i][j][k] = tbl[i-1][j][k]

        return tbl[len(strs)-1][m][n]


if __name__ == "__main__":
    s = Solution()
    print(s.findMaxForm(["10","0001","111001","1","0"],5,3))
    print(s.findMaxForm(["10","0001","111001","1","0"],4,3))