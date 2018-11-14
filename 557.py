class Solution:
	def reverseWords(self, s):
		"""
		:type s: str
		:rtype: str
		"""

		s1 = s.split()
		s = " ".join([i[::-1] for i in s1])
		return s