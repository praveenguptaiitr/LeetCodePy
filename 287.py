class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums)==0:
            return 0

        slow = nums[0]
        fast = nums[0]
        first = True
        while first != False or slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            first = False

        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

if __name__== "__main__":
    s = Solution()
    s.findDuplicate([1,3,4,2,2])