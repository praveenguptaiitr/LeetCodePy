from functools import cmp_to_key


def cmp_items(a1, b1):
	a = a1.split(" ",1)
	b = b1.split(" ",1)
	if not a[1][0].isdigit() and not b[1][0].isdigit():
		if (a[1] < b[1]):
			return -1
		elif (a[1] == b[1]):
			return a[0]<b[0]
		else :
			return 1


	if a[1][0].isdigit() and b[1][0].isdigit():
		return int(a[1][0])<int(b[1][0])
	if a[1][0].isdigit() and not b[1][0].isdigit():
		return 1
	if not a[1][0].isdigit() and b[1][0].isdigit():
		return -1

	return 0


class Solution:


	def reorderLogFiles(self, logs):
		"""
		:type logs: List[str]
		:rtype: List[str]
		"""
		cmp_items_py3 = cmp_to_key(cmp_items)

		logs.sort(key=cmp_items_py3)
		return logs

if __name__=="__main__":
	s = Solution()
	(s.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))