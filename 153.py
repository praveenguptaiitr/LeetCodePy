class Solution(object):

    def minHelper(self, nums, low, high):
        if low > high:
            return -1
        if nums[low] == nums[high]:
            return nums[low]

        if nums[low]< nums[high]:
            return nums[low]

        mid = (low + high)//2
        m1 = self.minHelper(nums, low, mid)
        m2 = self.minHelper(nums,mid+1,high)
        m3 = nums[mid]
        if m1 != -1 and m2 != -1:
            return min(m1,m2,m3)
        if m1 == -1 and m2 != -1:
            return min(m2,m3)

        return m3



    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return -1


        low = 0
        high = len(nums)-1
        if nums[low]< nums[high]:
            return nums[low]

        return self.minHelper(nums, 0, high)


if __name__ == "__main__":
    s = Solution()
    print(s.findMin([7,8,1,2,3,4,5,6]))