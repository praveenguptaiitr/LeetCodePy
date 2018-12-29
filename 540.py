class Solution(object):

    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        h = len(nums)-1
        if nums[0]!=nums[1]:
            return nums[0]

        if nums[h]!= nums[h-1]:
            return nums[h]

        while l<h:
            mid = (l+h)//2
            if mid ==0 and nums[mid]!= mid[mid+1]:
                return nums[mid]
            if mid == len(nums)-1 and nums[mid]!= nums[mid-1]:
                return nums[mid]
            if nums[mid-1]!= nums[mid] and nums[mid]!= nums[mid+1]:
                return nums[mid]

            if nums[mid]==nums[mid+1]:
                if mid%2 ==0:
                    l = mid+2
                else:
                    h=mid-1
            else:
                if nums[mid]!= nums[mid-1]:
                    return nums[mid]
                if mid%2 ==0:
                    h = mid-2
                else:
                    l=mid+1

        return nums[l]

if __name__ == "__main__":
    s = Solution()
    print(s.singleNonDuplicate([3,3,7,7,10,11,11]))