class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        for c in ",.\":\';@#!$%^&*-?><+\\|{}[]()`~":
            s = s.replace(c,"")

        l = s.split()
        s = "".join(l)
        #print(s)
        return s == s[::-1]


if __name__=="__main__":
    s = Solution()
    s.isPalindrome("A man, a plan, a canal: Panama")