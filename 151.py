class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()

        if len(s)==0:
            return ""

        s = s[::-1]
        return " ".join([i[::-1] for i in s.split()])