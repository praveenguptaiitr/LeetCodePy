class Solution(object):
	def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		maxEndHere = nums[0]
		maxSoFar = nums[0]
		for i in range(len(nums)):
			maxEndHere = max(nums[i], nums[i]+maxEndHere)
			maxSoFar = max(maxEndHere,maxSoFar)
		return maxSoFar

if __name__ == '__main__':
	s = Solution()
	print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

