class Solution(object):

    def trimHash(self, s):
        while "#" in s:
            if s[0]=="#":
                del s[0]
            for i in range(len(s)-1):
                if s[i+1]=="#":
                    del(s[i+1])
                    del(s[i])
                    break


        return s

    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        l1 = list(S)
        l2 = list(T)

        l1 = self.trimHash(l1)
        l2 = self.trimHash(l2)
        if l1 == l2:
            return True
        else:
            return False


if __name__=="__main__":
    s = Solution()
    print(s.backspaceCompare("a#c", "b"))