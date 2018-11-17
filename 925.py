class Solution:
	def isLongPressedName(self, name, typed):
		"""
		:type name: str
		:type typed: str
		:rtype: bool
		"""
		if name is None and typed is not None:
			return False
		if name is not None and typed is None:
			return False

		i = 0
		j = 0

		while (i < len(name) - 1):
			if name[i]!=typed[j]:
				return False
			while (i < len(name) and j < len(typed) and name[i] == typed[j]):
				i += 1
				j += 1
			while (j < len(typed) and typed[j] == typed[j - 1]):
				j+=1
			if i < len(name) and j >= len(typed):
				return False


		return True


if __name__ == "__main__":
	s = Solution()
	print(s.isLongPressedName("pyplrz","ppyypllr"))