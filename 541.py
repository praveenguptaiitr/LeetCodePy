class Solution(object):
	def reverseStr(self, s, k):
		"""
		:type s: str
		:type k: int
		:rtype: str
		"""
		l = list(s)
		l1 = [l[i:i+k] for i in range(0,len(s),k)]
		s = [l1[i].reverse() if i%2==0 else l1[i] for i in range(len(l1))]
		ans = ""
		for i in l1:
			ans+="".join(i)
		return ans

if __name__=='__main__':
	s = Solution()
	s.reverseStr("abcde",2)