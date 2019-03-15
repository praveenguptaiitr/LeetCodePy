class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)==0:
            return True
        if len(t)==0:
            return False
        i = 0
        j = 0
        for j in range(len(t)):
            if s[i]==t[j]:
                i+=1
            if i==len(s):
                break
        return i==len(s)