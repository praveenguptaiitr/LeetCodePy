class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0;
        j = len(nums) - 1
        k=0
        while(k<=j):
            if nums[k]==0:
                nums[i],nums[k]=nums[k],nums[i]
                i+=1
                k+=1
            elif nums[k]==1:
                k+=1
            elif nums[k]==2:
                nums[j],nums[k]=nums[k],nums[j]
                j-=1

        print(nums)


if __name__=="__main__":
    s = Solution()
    #s.sortColors([1,2,0,0,0,1,0,0,2])
    s.sortColors([1,2,0])