class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        if numRows ==2:
            return [[1],[1,1]]

        ans = [[1],[1,1]]
        for i in range(2, numRows):
            a = [1]*(i+1)
            for j in range(1,i):
                a[j]=ans[i-1][j-1]+ ans[i-1][j]
            ans.append(a)

        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.generate(5))