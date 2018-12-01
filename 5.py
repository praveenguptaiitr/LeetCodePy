class Solution:

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s)==0:
            return ""
        if len(s)==1:
            return s[0]
        if len(s)==2:
            if s[0]==s[1]:
                return s
            else:
                return s[0]

        n = len(s)
        start = 0
        end = 0
        sz = 1
        tbl = [[False]* len(s) for r in range(n)]
        for i in range(n):
            tbl[i][i]=True

        for i in range(n-1):
            if s[i]==s[i+1]:
                tbl[i][i+1]=True
                start = i
                end = i+1
                sz = 2

        for k in range(3, n+1):
            for i in range(0, n-k+1):
                j = i+k-1
                if tbl[i+1][j-1] and s[i]==s[j]:
                    tbl[i][j]=True
                    if k > sz:
                        start = i
                        end =j
                        sz = k

        return s[start:end+1]

if __name__=="__main__":
    s = Solution()
    k = s.longestPalindrome("abbc")
    print(k)