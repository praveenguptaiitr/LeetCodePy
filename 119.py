class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        if rowIndex==0:
            return []
        if rowIndex==1:
            return [[1]]
        if rowIndex ==2:
            return [1,1]

        ans = [[1],[1,1]]
        for i in range(2, rowIndex+1):
            a = [1]*(i+1)
            for j in range(1,i):
                a[j]=ans[i-1][j-1]+ ans[i-1][j]
            ans.append(a)

        return ans[-1]

if __name__ == "__main__":
    s = Solution()
    print(s.getRow(3))
