class Solution(object):

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        if len(s)==2:
            if s[0]==s[1]:
                return 3
            else:
                return 2
        count = 0
        n = len(s)-1
        dp = [[False]*len(s) for a in range(len(s))]
        for i in range(n+1):
            dp[i][i]=True
            count+=1

        for i in range(n):
            if s[i]==s[i+1]:
                dp[i][i+1]=True
                count+=1

        for k in range(2,n+1):
            for i in range(n-k+1):
                j = i+k
                if i==j:
                    dp[i][j]=True
                if s[i]==s[j]:
                    if i+1<n:
                        dp[i][j]= dp[i+1][j-1]
                if s[i]!= s[j]:
                    dp[i][j]=False
                if dp[i][j]==True:
                    count+=1

        return count


if __name__ == "__main__":
    s = Solution()
    print(s.countSubstrings("aba"))
    print(s.countSubstrings("abc"))
    print(s.countSubstrings("aaa"))