class Solution(object):
	def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""

		if len(nums) == 0:
			return 0
		if len(nums) == 1:
			return nums[0]

		maxEndHere = nums[0]
		maxSoFar = nums[0]
		for i in range(1,len(nums)):
			maxEndHere = max(nums[i], nums[i] + maxEndHere)
			maxSoFar = max(maxEndHere, maxSoFar)
		return maxSoFar


if __name__ == '__main__':
	s = Solution()
	print(s.maxSubArray([1,2]))

