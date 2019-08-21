class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        ws = set(wordDict)
        if len(s) == 0:
            return 0

        dp = [False]*(len(s)+1)
        dp[0]=True
        for i in range(len(dp)):
            for j in range(i):
                if dp[j] and s[j:i] in ws:
                    dp[i]=True

        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.wordBreak("leetcode", ["leet", "code"]))
    print(s.wordBreak("applepenapple", ["apple", "pen"]))
    print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))