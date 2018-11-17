class Solution(object):
	def canConstruct(self, ransomNote, magazine):
		"""
		:type ransomNote: str
		:type magazine: str
		:rtype: bool
		"""
		d = {}
		for i in range(len(magazine)):
			d[magazine[i]] = d.get(magazine[i],0)+1
		for i in range(len(ransomNote)):
			if ransomNote[i] not in d:
				return False
			d[ransomNote[i]] = d.get(ransomNote[i],0)-1
			if d[ransomNote[i]] < 0:
				return False

		return True
