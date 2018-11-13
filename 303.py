class NumArray:

	def __init__(self, nums):
		"""
		:type nums: List[int]
		"""
		self.nums = nums
		self.sum = [0]* len(nums)
		self.sum[0]= nums[0]
		for i in range(1,len(self.sum)):
			self.sum[i]+=self.sum[i-1]+nums[i]

	def sumRange(self, i, j):
		"""
		:type i: int
		:type j: int
		:rtype: int
		"""
		if self.nums is None:
			return 0
		return self.sum[j]-self.sum[i]+ self.nums[i]


if __name__ == "__main__":
	s = NumArray([-2, 0, 3, -5, 2, -1])
	print(s.sumRange(0,5))
