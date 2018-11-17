class Solution(object):
	def lengthOfLastWord(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		s = s.strip()
		ans = len(s)
		for i in range(len(s)-1, -1, -1):
			if s[i] == " ":
				ans = len(s) - i-1
				break

		return ans


if __name__ == "__main__":
	s = Solution()
	print(s.lengthOfLastWord("Hello World"))