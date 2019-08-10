class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dq = []
        ans = []
        n = len(nums)
        for i in range(n):
            while(len(dq)>0 and dq[-1][0] < nums[i]):
                dq.pop()

            dq.append((nums[i], i))

            while(dq[0][1]== i-k):
                dq.pop(0)

            #print(dq)
            if i+1-k >= 0:
                ans.append(dq[0][0])


        return ans




if __name__ == "__main__":
    s = Solution()
    print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
    print(s.maxSlidingWindow([7,2,4], 2))
    print(s.maxSlidingWindow([1,3,1,2,0,5],3))