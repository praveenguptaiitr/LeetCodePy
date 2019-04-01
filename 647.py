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
        for d in range(len(s)):
            for i in range(len(s)-d):
                j = i+d
                if s[i]==s[j]:
                    dp[i][j]= True if i+1>= j-1 else dp[i+1][j-1]
                if s[i]!= s[j]:
                    dp[i][j]=False
                if dp[i][j]==True:
                    count+=1

        return count


if __name__ == "__main__":
    s = Solution()
    print(s.countSubstrings("aaa"))