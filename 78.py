class Solution(object):

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums)==0:
            return []

        if len(nums)==1:
            return [[],[nums[0]]]

        d = {}

        m = 2**len(nums)
        for i in range(m):
            s = bin(i)
            s = s[2:]
            s = s[::-1]
            ans = []
            for j in range(len(s)):
                if s[j]=="1":
                    ans.append((nums[j]))

            k = [str(i) for i in ans]
            p = "".join(sorted(k))
            d[p]= ans

        return d.values()
