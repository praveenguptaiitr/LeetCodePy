class Solution:

    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        #level=1
        return [k for k in range(int((2*n) ** 0.5)-1, int((2*n) ** 0.5)+1) if k*(k+1)/2 <= n and n < (k+1)*(k+2)/2][0]


    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if ( len(nums1)<len(nums2)):
            smaller = nums1
            larger = nums2
        else:
            smaller = nums2
            larger = nums1

        si = 0

        while(si < len(smaller)):
            li = si+1
            while(li<len(larger)):
                if smaller[si]==larger[li]:
                    while(smaller[si]==larger[li]):
                        si = si+1
                        li = li+1




if __name__=='__main__':
    s = Solution()
    print(s.arrangeCoins(1))