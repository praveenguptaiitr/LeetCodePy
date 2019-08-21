class Solution(object):

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 1

        dp = [0]*(len(s)+1)
        dp[0]=1
        dp[1]=0 if s[0]=="0" else 1


        for i in range(2,len(s)+1):
            if 1<=int(s[i-1])<=9:
                dp[i]+=dp[i-1]
            if 10<=int(s[i-2]+s[i-1])<=26:
                dp[i]+=dp[i-2]


        return dp[-1]





if __name__ == "__main__":
    s = Solution()
    print(s.numDecodings("226"))
    print(s.numDecodings("101"))
    print(s.numDecodings("00"))
    print(s.numDecodings("27"))