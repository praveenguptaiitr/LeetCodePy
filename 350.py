class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        d1 = {}
        d2 = {}

        for n in nums1:
            d1[n]=d1.get(n,0)+1

        for n in nums2:
            d2[n]=d2.get(n,0)+1

        ans = []
        for n in d1.keys():
            f1 = d1[n]
            f2 = d2.get(n,0)
            m = min(f1,f2)
            if m > 0:
                for i in range(m):
                    ans.append(n)


        return  ans