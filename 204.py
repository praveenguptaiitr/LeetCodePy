class Solution:
    def findKth(self, nums1, nums2, k):
        if len(nums1)==0:
            return nums2[k]
        if len(nums2)==0:
            return nums1[k]

        mid1 = len(nums1)//2
        mid2 = len(nums2)//2

        if  k > mid1+mid2:
            if nums1[mid1]>nums2[mid2]:
                return self.findKth(nums1, nums2[mid2+1:], k-mid2-1)
            else:
                return self.findKth(nums1[mid1+1:], nums2, k-mid1-1)
        else:
            if nums1[mid1]> nums2[mid2]:
                return self.findKth(nums1[:mid1],nums2,k)
            else:
                return self.findKth(nums1, nums2[:mid2], k)


    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)

        if (m+n)%2 == 0:
            x1 = self.findKth(nums1, nums2, (m+n)//2)
            x2 = self.findKth(nums1, nums2, ((m+n)//2) - 1)
            return float((x1+x2))/2

        else:
            return float(self.findKth(nums1, nums2, (m+n)//2))


if __name__ == "__main__":
    s = Solution()
    #print(s.findMedianSortedArrays([1,3,8,9,15],[7,11,18,19,21,25]))
    print(s.findMedianSortedArrays([], [2,3]))