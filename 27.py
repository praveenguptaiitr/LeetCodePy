class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums)==0:
            return 0
        if len(nums)==1 and nums[0]==val:
            return 0
        if len(nums)==1 and nums[0]!=val:
            return 1


        i = 0
        j = len(nums)-1
        while i < j:
            while(i < len(nums) and nums[i]!=val):
                i+=1
            while(j >= 0 and nums[j]==val):
                j-=1
            if (i<j):
                nums[i],nums[j]=nums[j],nums[i]
        k = len(nums)-1
        while(k>=0 and nums[k]==val):
            k-=1
        return k+1


if __name__=='__main__':
    s = Solution()
    nums=[0,1,2,2,3,0,4,2]
    print(s.removeElement(nums,2))