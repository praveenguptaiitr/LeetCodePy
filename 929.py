class Solution(object):
	def numUniqueEmails(self, emails):
		"""
		:type emails: List[str]
		:rtype: int
		"""
		ans = set()
		if len(emails) == 0 :
			return []

		for e in emails:
			l = e.split("@")
			x = l[0].find("+")
			if x != -1:
				l[0]=l[0][:x]

			l[0]=l[0].replace(".","")
			ans.add(l[0]+"@"+l[1])

		return len(ans)


if __name__ == "__main__":
	s = Solution()
	print(s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
