class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        if len(nums)==0:
            return 1

        if len(nums)==1 and nums[0]!=1:
            return 1

        if len(nums)==1 and nums[0]==1:
            return 2


        isOnePresent = False
        for i in range(n):
            if nums[i]==1:
                isOnePresent = True

        if isOnePresent == False:
            return 1

        for i in range(n):
            if nums[i]<=0 or nums[i]>n:
                nums[i]=1


        for i in range(n):
            v = abs(nums[i])
            if v==n:
                nums[0]=-1*abs(nums[0])
            else:
                nums[v] = -1 * abs(nums[v])

        for i in range(1, n):
            if nums[i]>0:
                return i

        if nums[0]>0:
            return n

        return n+1

if __name__ == "__main__":
    s = Solution()
    # print(s.firstMissingPositive([3,4,-1,1]))
    # print(s.firstMissingPositive([7,8,9,11,12]))
    print(s.firstMissingPositive([1,2,0]))
    # print(s.firstMissingPositive([-2, -1]))
    # print(s.firstMissingPositive([1000, -1]))