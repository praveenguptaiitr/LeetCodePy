class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if len(nums)<k:
            return 0

        i = k
        sums = 0
        sums = sum(nums[:k])
        max_avg = sums/k
        avg = max_avg

        while i < len(nums):
            sums = sums+nums[i]-nums[i-k]
            avg= sums/k

            if avg > max_avg:
                max_avg=avg
            i = i + 1

        return max(max_avg, sums/k)

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        k = len(nums1)-1
        m = m-1
        n = n-1
        while(m>=0 and n>=0):
            if nums1[m]>nums2[n]:
                nums1[k]=nums1[m]
                m = m-1
            else:
                nums1[k]=nums2[n]
                n = n - 1
            k = k - 1

        if m <= 0:
            while n>=0:
                nums1[k]=nums2[n]
                k = k -1
                n = n - 1
        if n <= 0:
            while m >= 0:
                nums1[k]=nums1[m]
                k = k - 1
                m = m - 1

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums) == 0):
            return 0

        i = 0
        j = i + 1
        # flag = False
        while True:
            while j < len(nums) and i < len(nums) and nums[i] == nums[j]:
                j = j + 1
            if (i <= len(nums) - 2) and j < len(nums):
                nums[i + 1] = nums[j]

            i = i + 1
            if i >= len(nums) or j >= len(nums):
                break
        return i


if __name__ == "__main__":
    s = Solution()
    #print(s.findMaxAverage([-5], 1))
    #s.merge([0],0,[1],1)
    print(s.removeDuplicates([1,1,2]))