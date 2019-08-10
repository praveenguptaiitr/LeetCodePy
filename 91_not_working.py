class Solution(object):
    def __init__(self):
        self.tbl = {}

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        self.tbl["0"]=0
        for i in range(1,27):
            if i <=9:
                self.tbl[str(i)]=1
            else :
                self.tbl[str(i)]=2

        self.helper(s)
        return self.tbl[s]

    def helper(self, s):
        if len(s)==0:
            self.tbl[s]=0
            return 0

        if s in self.tbl:
            return self.tbl[s]

        for i in range(1,len(s)):
            print(s[:i] + " -- " + s[i:])

            self.tbl[s]= self.tbl.get(s,0) + self.helper(s[:i]) * self.helper(s[i:])

        self.tbl[s]-=1

        return self.tbl[s]





if __name__ == "__main__":
    s = Solution()
    print(s.numDecodings("12"))
    print(s.numDecodings("226"))