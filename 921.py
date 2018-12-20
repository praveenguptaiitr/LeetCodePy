class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """

        if len(S)==0:
            return 0

        l = []
        for i in S:
            if i == "(":
                l.append(i)
            elif len(l) > 0 and i == ")" and l[len(l)-1]=="(":
                l.pop()
            else:
                if i == ")":
                    l.append(")")

        return len(l)

if __name__ == "__main__":
    s = Solution()
    print(s.minAddToMakeValid("())"))
    print(s.minAddToMakeValid("((("))
    print(s.minAddToMakeValid("()"))
    print(s.minAddToMakeValid("()))(("))
