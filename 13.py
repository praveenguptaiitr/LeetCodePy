class Solution(object):
	def romanToInt(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		if not s:
			return 0
		no = 0
		i = 0
		d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
		#jump = False
		while i <= len(s)-1:
			#jump=False
			if i+1< len(s) and s[i]=='I' and s[i+1]=='V':
				no+=4
				i+=2
				#jump=True
				continue
			if i+1< len(s) and s[i] == 'I' and s[i + 1] == 'X':
				no+=9
				i+=2
				#jump = True
				continue
			if i+1< len(s) and s[i]=='X' and s[i+1]=='L':
				no+=40
				i+=2
				#jump = True
				continue
			if i+1< len(s) and s[i] == 'X' and s[i + 1] == 'C':
				no+=90
				i+=2
				#jump = True
				continue
			if i+1< len(s) and s[i] == 'C' and s[i + 1] == 'D':
				no+=400
				i+=2
				#jump = True
				continue
			if i+1< len(s) and s[i] == 'C' and s[i + 1] == 'M':
				no+=900
				i+=2
				#jump = True
				continue

			no+=d[s[i]]
			i+=1
		return no

if __name__=='__main__':
	s = Solution()
	print(s.romanToInt("MDCXCV"))