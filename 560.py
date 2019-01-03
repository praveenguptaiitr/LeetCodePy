class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum = 0
        count = 0
        d = {}
        d[0]=1
        for i in range(len(nums)):
            sum+=nums[i]
            if sum-k in d.keys():
                count+=d[sum-k]
            d[sum] = d.get(sum,0)+1
        return count