class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        if n == 0:
            return [0]
        if n == 1:
            return [0,1]
        if n == 2:
            ans = ["00","01","11","10"]
            return [int(i,2) for i in ans]

        ans = ["00","01","11","10"]
        for j in range(3,n+1):
            ans1 = [ "0"+str(i) for i in ans]
            ans2 = reversed(ans)
            ans2 = [ "1"+str(i) for i in ans2]
            ans = ans1 + ans2

        return [int(i,2) for i in ans]

if __name__=="__main__":
    s = Solution()
    print(s.grayCode(3))
