class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        st = []
        maxArea = 0
        n = len(heights)
        i = 0
        while i < n:
            if len(st) == 0 or heights[i] > heights[st[-1]]:
                st.append(i)
                i += 1
            else:
                top = st.pop()
                if len(st) > 0:
                    maxArea = max(maxArea, heights[top] * (i - st[-1] - 1))
                else:
                    maxArea = max(maxArea, heights[top] * (i))

        while (len(st) > 0):
            top = st.pop()
            if len(st) > 0:
                maxArea = max(maxArea, heights[top] * (i - st[-1] - 1))
            else:
                maxArea = max(maxArea, heights[top] * (i))

        return maxArea


if __name__ == "__main__":
    s = Solution()
    print(s.largestRectangleArea([2,1,5,6,2,3]))