class Solution(object):
	def reverseVowels(self, s):
		"""
		:type s: str
		:rtype: str
		"""

		v = ["a","e","i","o","u","A","E","I","O","U"]
		i = 0
		j = len(s)-1
		n = len(s)
		s1 = list(s)
		while i < j:
			while i < n and s1[i] not in v:
				i+=1
			while j > 0 and s1[j] not in v:
				j-=1
			if i < j and s1[i] in v and s1[j] in v :
				s1[i],s1[j]=s1[j],s1[i]
				i+=1
				j-=1

		return "".join(s1)

if __name__ == "__main__":
	s = Solution()
	print(s.reverseVowels(".,"))
