class Solution(object):

    def bsearch(self,nums, low, high, target):
        if(low>high):
            return -1
        if low==high:
            if nums[low]==target:
                return low
            else:
                return -1
        if nums[low]==target:
            return low
        if nums[high]==target:
            return high

        mid=int((low+high)/2)
        if nums[mid]==target:
            return mid

        if nums[low]<nums[high]: #simple sorted no pivot
            if nums[mid]>target:
                return self.bsearch(nums,low,mid-1,target)
            else:
                return self.bsearch(nums,mid+1,high,target)

        if(nums[mid]<nums[low]): #pivot on left
            if(target>nums[mid] and target<nums[high]):
                return self.bsearch(nums,mid+1,high,target)
            else:
                return self.bsearch(nums, low, mid-1, target)
        if(nums[mid]>nums[high]): #pivot on right
            if(target>nums[low] and target<nums[mid]):
                return self.bsearch(nums,low,mid-1,target)
            else:
                return self.bsearch(nums,mid+1,high,target)

        return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.bsearch(nums,0,len(nums)-1, target)

if __name__== '__main__':
    s = Solution()
    print(s.search([1,2,3,4,5,6],4))