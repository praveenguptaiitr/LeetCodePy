class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        i=0
        jumps = 0
        end = 0
        e = 0
        n = len(nums)-1
        if (len(nums)==0 or len(nums)==1):
            return 0

        for i in range(0,n):
            e = max(e, i+nums[i])
            if(i==end):
                jumps+=1
                end = e

        return jumps

if __name__ == "__main__":
    s = Solution()
    print(s.jump([2,3,1,1,4]))