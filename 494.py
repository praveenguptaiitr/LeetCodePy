class Solution(object):
    def __init__(self):
        self.tbl = []
        self.nums = []
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.nums = nums
        self.tbl = [[float("-inf")] * 2001 for _ in range(len(nums))]
        return self.helper(0,0,S)

    def helper(self, i, s, S):
        if i == len(self.nums):
            if s == S:
                return 1
            else:
                return 0

        else:
            if self.tbl[i][s+1000]!= float("-inf"):
                return self.tbl[i][s+1000]

            add = self.helper(i+1, s + self.nums[i], S)
            subtr = self.helper(i+1, s - self.nums[i], S)

            self.tbl[i][s+1000] = add + subtr
            return self.tbl[i][s+1000]


if __name__ == "__main__":
    s = Solution()
    print(s.findTargetSumWays([1, 1, 1, 1, 1],3))