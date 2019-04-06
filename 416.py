class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s%2 != 0:
            return False
        s = s//2+1
        tbl = [[False]*s for i in nums]
        tbl[0][0]=True
        for i in range(1,len(nums)):
            tbl[i][0]=True

        for i in range(len(nums)):
            for j in range(s):
                if j-nums[i]>=0:
                    tbl[i][j]= tbl[i-1][j-nums[i]] or tbl[i-1][j]

        return tbl[len(nums)-1][s-1]


if __name__ == "__main__":
    s = Solution()
    print(s.canPartition([1, 5, 11, 5]))