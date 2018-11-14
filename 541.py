class Solution(object):
	def reverseStr(self, s, k):
		"""
		:type s: str
		:type k: int
		:rtype: str
		"""
		l = s.split()
		s = [ l[i][::-1] if i%2==0 else l[i] for i in range(len(l))]
		ans=" ".join(s)
		return ans

if __name__=='__main__':
	s = Solution()
	s.reverseStr("abc def ghi jkl",2)