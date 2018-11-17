from collections import defaultdict
class Solution(object):
	def isIsomorphic(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""

		d1 = defaultdict(list)
		d2 = defaultdict(list)
		d11 = {}
		d22 = {}
		for i in range(len(s)):
			if s[i] not in d11:
				d11[s[i]]=i
			d1[d11[s[i]]].append(i)
		for i in range(len(t)):
			if t[i] not in d22:
				d22[t[i]]=i
			d2[d22[t[i]]].append(i)

		ans = True
		for (k,v) in d11.items():
			if d1.get(v,[])!= d2.get(v,[]):
				return False

		for (k,v) in d22.items():
			if d1.get(v,[])!= d2.get(v,[]):
				return False

		return True


if __name__ == "__main__":
	s = Solution()
	print(s.isIsomorphic("title", "paper"))