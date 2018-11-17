class Solution(object):
	def compress(self, chars):
		"""
		:type chars: List[str]
		:rtype: int
		"""

		if len(chars)==1:
			return 1
		s = 0
		freq = 1
		i = 0
		while i < len(chars)-1:
			if chars[i]!=chars[i+1]:
				chars[s]=chars[i]
				if freq == 1:
					s+=1
					i+=1
					continue
				if freq>1:
					chars[s]=chars[i]
					s+=1
					s1 = str(freq)
					for x in s1:
						chars[s]=x
						s+=1
				freq = 1
			else:
				freq+=1
			i+=1


		if freq == 1:
			chars[s ] = chars[len(chars) - 1]
			s+=1
		if freq > 1:
			chars[s] = chars[len(chars) - 1]
			s += 1
			s1 = str(freq)
			for x in s1:
				chars[s] = x
				s += 1
		return s

if __name__=="__main__":
	s = Solution()
	print(s.compress(["a","a","a","a","a","b"]))


