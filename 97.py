class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if (len(s1)+ len(s2))!= len(s3):
            return False

        if len(s1)==0:
            if s2==s3:
                return True
            else:
                return False

        if len(s2)==0:
            if s1==s3:
                return True
            else:
                return False

        s1 = " " + s1
        s2 = " " + s2
        s3 = " " + s3


        tbl = [[False]*(len(s2)+1) for i in range(len(s1)+1)]

        tbl[0][0]=True
        for i in range(1,len(s2)):
            if s3[i]==s2[i]:
                tbl[0][i]= tbl[0][i-1]
        for i in range(1,len(s1)):
            if s3[i]==s1[i]:
                tbl[i][0]= tbl[i-1][0]

        for i in range(1,len(s1)):
            for j in range(1,len(s2)):
                if s3[i+j]==s1[i] and s3[i+j]==s2[j]:
                    tbl[i][j] = tbl[i - 1][j] or tbl[i][j-1]
                elif s3[i+j] == s1[i]:
                    tbl[i][j]=tbl[i-1][j]
                elif s3[i+j] == s2[j]:
                    tbl[i][j]=tbl[i][j-1]


        return tbl[len(s1)-1][len(s2)-1]

if __name__=="__main__":
    s = Solution()
    print(s.isInterleave("aab", "axy", "aaxaby"))
    print(s.isInterleave("aab", "axy", "abaaxy"))

    print(s.isInterleave("aabc","abad","aabadabc"))
    print(s.isInterleave("db","b","cbb"))
    #
    print(s.isInterleave("aabaac","aadaaeaaf","aadaaeaabaafaac"))