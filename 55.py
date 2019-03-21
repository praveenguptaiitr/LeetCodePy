class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        start = 0
        end = nums[0]
        endMax = start
        n = len(nums)-1
        while(end<=n):
            for i in range(start, end+1):
                if start == end:
                    return False
                endMax = max(endMax,i+nums[i])
            if endMax>=n:
                return True
            start = end
            end = endMax
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.canJump([2,3,1,1,4]))
    print(s.canJump([3,2,1,0,4]))
    print(s.canJump([1]))