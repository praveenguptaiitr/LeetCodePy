class Solution:

    def findLongest(self,str, tbl,i,j):
        if i > j:
            return -1

        if tbl[i][j]!=-1:
            return tbl[i][j]

        if str[i]==str[j]:
            tbl[i][j]= 2+self.findLongest(str,tbl,i+1,j-1)
        else:
            l1,l2 = -1,-1
            l1=self.findLongest(str,tbl,i+1,j)
            l2= self.findLongest(str,tbl,i,j-1)
            tbl[i][j]=max(l1,l2)

        return tbl[i][j]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None :
            return 0

        tbl = [ [-1]*(len(s)) for i in range(len(s))]
        for i in range(len(s)):
            tbl[i][i]=1
        p = self.findLongest(s,tbl,0,len(s)-1)
        return tbl

if __name__=="__main__":
    s = Solution()
    k = s.longestPalindrome("babad")
    print(k)