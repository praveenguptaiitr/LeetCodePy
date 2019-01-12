class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = 0
        for n1 in nums:
            n ^=n1

        mask = 1
        while(mask & n ==0):
            mask<<=1

        a=0
        b=0
        for n1 in nums:
            if n1 & mask ==0:
                a^=n1
            else:
                b^=n1

        return [a,b]
