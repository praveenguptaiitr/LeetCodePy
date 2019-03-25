class Solution(object):
    def isPalin(self,s):
        return s==s[::-1]

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i=0
        j = len(s)-1
        while(i<j):
            if s[i]!=s[j]:
                return self.isPalin(s[i:j]) or self.isPalin(s[i+1:j+1])
            i+=1
            j-=1
        return True
