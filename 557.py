class Solution:
	def reverseWords(self, s):
		"""
		:type s: str
		:rtype: str
		"""

		# s1 = s.split()
		# s = " ".join([i[::-1] for i in s1])
		# return s

		i=0
		ss = 0
		se = 0
		while(i<len(s)):
			while(i < len(s) and s[i]==" "):
				i+=1
			ss = i
			while(i < len(s) and s[i]!= " "):
				i+=1
			se = i
			s1 = s[0:ss]+ s[ss:se][::-1]+s[se:]
			s = s1

		return s

if __name__ == "__main__":
	s = Solution()
	print(s.reverseWords("abc     efg   hij"))