class Solution(object):
	def checkRecord(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		idx = -1
		count1 = 0
		count2 = 0
		while(True):
			a = s.find('A',idx+1)
			if a !=-1:
				idx = a
				count1+=1
			else:
				break
		idx = -1
		while(True):
			a = s.find('LLL',idx+1)
			if a !=-1:
				idx = a
				count2+=1
			else:
				break

		if count1<=1 and count2==0:
			return True
		else:
			return False



if __name__=="__main__":
	s = Solution()
	print(s.checkRecord("LLPPPLL"))