class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        #s = " " + s
        n = len(s)

        if n==0 or n==1:
            return n
        if n==2:
            if s[0]==s[1]:
                return 2
            else:
                return 1
        tbl = [[0]*n for i in range(n)]
        for i in range(n):
            tbl[i][i]=1

        for d in range(1,n):
            for i in range(0,n-d):
                j = i+d
                if s[i]==s[j]:
                    tbl[i][j]=2+tbl[i+1][j-1]
                else:
                    tbl[i][j]= max(tbl[i][j-1], tbl[i+1][j])

        return tbl[0][n-1]

if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindromeSubseq("madam"))
    print(s.longestPalindromeSubseq("bbbab"))
    print(s.longestPalindromeSubseq("cbbd"))