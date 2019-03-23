class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)==2:
            return 1*min(height)
        i=0
        j = len(height)-1
        m = 0
        while(i<j):
            w = min(height[i],height[j])*(abs(i-j))
            m=max(w,m)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1

        return m

if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))