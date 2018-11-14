class Solution:
	def rotateString(self, A, B):
		"""
		:type A: str
		:type B: str
		:rtype: bool
		"""
		if not A and not B:
			return True
		if not A:
			return False
		if not B:
			return False
		for i in range(len(A)):
			s1 = A[-i:] + A[:len(A) - i]
			if s1 == B:
				return True

		return False
