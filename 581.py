class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0 or len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 2 if nums[0] > nums[1] else 0

        l = len(nums)
        s = -1
        e = -1
        for i in range(0, l - 1):
            if nums[i+1] < nums[i]:
                s=i
                break

        if s == -1:
            return 0


        for j in range(l - 1, 0, -1):
            if nums[j-1] > nums[j]:
                e =j
                break


        idxmin=0
        idxmax=0
        m1 = float('Inf')
        m2 = -float('Inf')

        for i in range(s,e+1):
            if nums[i]< m1:
                idxmin = i
                m1 = nums[i]
            if nums[i] > m2:
                idxmax = i
                m2 = nums[i]

        l=0
        r=0
        for k in range(s+1):
            if nums[k]>m1:
                l=k
                break

        for k in range(len(nums)-1,e-1,-1):
            if nums[k]<m2:
                r=k
                break

        return r-l+1



if __name__ == "__main__":
    s = Solution()
    print(s.findUnsortedSubarray([2,1,1,1,1]))

