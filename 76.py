class Solution(object):
	def minWindow(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: str
		"""

		d = {}
		for c in t:
			d[c]=d.get(c,0)+1

		ctr = len(d)
		begin = 0
		end = 0
		l = 999999
		ans = ""
		while end < len(s):
			if s[end] in d:
				d[s[end]] = d[s[end]] -1
				if d[s[end]] == 0:
					ctr -=1

			end +=1
			while(ctr == 0):
				if (end-begin< l):
					l = end-begin
					ans = s[begin:end]

				p = s[begin]
				if p in d:
					d[p]+=1
					if d[p]>0:
						ctr+=1
				begin+=1

		return ans


if __name__ == "__main__":
	s = Solution()
	print(s.minWindow("ABAACBAB", "ABC"))
