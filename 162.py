class Solution(object):

    def peak(self, nums, l, h):
        if l>h:
            return -1

        if l==0 and nums[0]>nums[1]:
            return 0
        if h==len(nums)-1 and nums[h]>nums[h-1]:
            return h

        if l==h and l!=0 and l!= len(nums)-1:
            if nums[l-1]< nums[l] and nums[l]> nums[l+1]:
                return l

        mid = (l+h)//2
        if mid > 0 and mid < len(nums)-1 and nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
            return mid

        if mid > 0 and mid < len(nums)-1 and nums[mid]>nums[mid-1] and nums[mid]<nums[mid+1]:
            return self.peak(nums, mid+1, h)

        if mid > 0 and mid < len(nums)-1 and nums[mid]<nums[mid-1] and nums[mid]>nums[mid+1]:
            return self.peak(nums, l,mid-1)

        if mid ==0 :
            return self.peak(nums, mid + 1, h)
        if mid >0 and mid < len(nums)-1 and nums[mid]<nums[mid-1] and nums[mid]<nums[mid+1]:
            l1 = self.peak(nums, mid+1, h)
            if l1 != -1 :
                return l1
            l2 = self.peak(nums, mid+1, h)
            if l2!=-1:
                return l2
        return -1


    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums)==0:
            return -1
        if len(nums)==1:
            return 0

        if len(nums)==2:
            if nums[0]>nums[1]:
                return 0
            else:
                return 1

        return self.peak(nums, 0, len(nums)-1)

if __name__ =="__main__":
    s = Solution()
    print(s.findPeakElement([1,2,1,2,1]))