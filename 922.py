class Solution:
	def sortArrayByParityII(self, A):
		"""
		:type A: List[int]
		:rtype: List[int]
		"""
		i = 0
		j = 1
		while (i < len(A) and j < len(A)):
			while (i < len(A) and A[i] % 2 == 0):
				i += 2
			while (j < len(A) and A[j] % 2 != 0):
				j += 2
			if i < len(A) and j < len(A):
				A[i], A[j] = A[j], A[i]
		return A

