class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        m = len(word1)
        n = len(word2)

        if m ==0 and n==0:
            return 0

        if m == 0 and n!= 0:
            return n

        if n ==0 and m !=0:
            return m

        word1 = " " + word1
        word2 = " " + word2

        tbl = [[0]*(len(word1)+1) for _ in range(len(word2)+1)]

        for i in range(len(word1)):
            tbl[0][i]=i

        for j in range(len(word2)):
            tbl[j][0]=j

        for i in range(1,len(word2)):
            for j in range(1,len(word1)):
                if word2[i]==word1[j]:
                    tbl[i][j] = tbl[i-1][j-1]
                else:
                    tbl[i][j] = min(tbl[i-1][j], tbl[i][j-1])+1

        return tbl[len(word2)-1][len(word1)-1]



if __name__ == "__main__":
    s = Solution()
    print(s.minDistance("a", "ab"))
    print(s.minDistance("sea", "eat"))