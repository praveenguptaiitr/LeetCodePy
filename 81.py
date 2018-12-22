class Solution:
    def bsearch(self, nums, l, r, x):
        if l > r:
            return False

        if l == r :
            if nums[l]==x:
                return True
            else:
                return False

        if nums[l]==x:
            return True

        if nums[r]==x:
            return True


        mid = int((l+r)/2)

        if nums[mid]==x:
            return True

        if nums[l]==nums[r]:
            return self.bsearch(nums, l+1, r-1, x)
        if nums[l]<nums[r]:
            if nums[mid]>x:
                return self.bsearch(nums,l,mid-1,x)
            else:
                return self.bsearch(nums,mid+1,r,x)

        if nums[mid]<nums[l]: #pivot on left
            if x > nums[mid] and x < nums[r]:
                return self.bsearch(nums, mid+1, r, x)
            else:
                return self.bsearch(nums, l, mid-1, x)

        if nums[mid]>nums[r]: #pivot on right
            if x > nums[l] and x < nums[mid]:
                return self.bsearch(nums, l, mid-1, x)
            else:
                return self.bsearch(nums, mid+1, r, x)

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        return self.bsearch(nums,0, len(nums)-1, target)

if __name__== '__main__':
    s = Solution()
    print(s.search([1,3],3))