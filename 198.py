class Solution:
    def do(self, nums, dp=None):
        if dp is None:
            dp = {}

        if (len(nums))==0:
            return 0
        i = len(nums)-1
        if i in dp:
            return dp[i]

        dp[i] = max(nums[i]+ self.do(nums[:-2], dp), self.do(nums[:-1], dp))

        return dp[i]

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.do(nums)

if __name__=="__main__":
    s = Solution()
    print(s.rob([1,2,3,1]))