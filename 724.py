class Solution:
	def pivotIndex(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""

		if len(nums)==0:
			return -1

		#if nums[0]== sum(nums[1:]):
		#	return 0
		ls = 0
		piv = 0
		rs = sum(nums)-nums[piv]-ls
		if ls == rs:
			return 0
		for piv in range(1,len(nums)):
			ls +=nums[piv-1]
			rs -=nums[piv]
			if ls == rs :
				return piv

		return -1

if __name__ == "__main__":
	s = Solution()
	print(s.pivotIndex([-1,-1,0,1,1,0]))
