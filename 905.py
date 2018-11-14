class Solution:
	def sortArrayByParity(self, A):
		"""
		:type A: List[int]
		:rtype: List[int]
		"""
		A.sort(key = lambda x : 1 if x%2 !=0 else -1)
		return A

if __name__ == "__main__":
	s = Solution()
	print(s.sortArrayByParity([1,2,2,2,6,7,8,9]))