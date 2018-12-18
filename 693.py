class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n <= 1:
            return True
        if n == 2:
            return True

        s = "{0:b}".format(n)
        o = s[0]
        if o is "0":
            t = "1"
        else:
            t = "0"

        ans = True
        for i in range(0,len(s)-1,2):
            if s[i]==o and s[i+1]==t:
                continue
            else:
                return False

        if len(s)>2:
            return ans and s[len(s)-1]!= s[len(s)-2]
        else:
            return ans