class Solution(object):
	def firstUniqChar(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		d = {}
		n = len(s)
		l = [-1]*n
		for i in range(len(s)):
			if s[i] not in d:
				d[s[i]] = i
				l[i]=i
			else:
				l[d[s[i]]]=-1

		for i in range(len(s)):
			if l[i]!=-1:
				return l[i]

		return -1
