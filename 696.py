class Solution(object):
	def countBinarySubstrings(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		groups = [1]
		for i in range(1,len(s)):
			if s[i]!=s[i-1]:
				groups.append(1)
			else:
				groups[-1]+=1

		ans = 0
		for i in range(len(groups)-1):
			ans+=min(groups[i],groups[i+1])

		return ans

if __name__=="__main__":
	s = Solution()
	print(s.countBinarySubstrings("110001111000000"))