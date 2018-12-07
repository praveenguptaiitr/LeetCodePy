class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1

        l=1
        m=0
        i=0
        j=1
        while(i<len(nums)-1):
            while(i < len(nums)-1 and nums[i]<nums[i+1]):
                l+=1
                i+=1
            m = max(m,l)
            l=1
            i=i+1
        return m

if __name__ == "__main__":
    s = Solution()
    print(s.findLengthOfLCIS([1,3,5,4,2,3,4,5]))