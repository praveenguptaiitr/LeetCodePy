class Solution(object):
    def __init__(self):
        self.ans = []

    def construct_candidates(self, arr, k, n):
        c = []
        for i in range(n):
            possible = True
            for j in range(k):
                if i == arr[j]:
                    possible = False
                if abs(k-j) == abs(i-arr[j]):
                    possible = False
            if possible == True:
                c.append(i)
        return c

    def bt(self, arr, k, n):
        if k == n:
            mz = [["."] * n for i in range(n)]
            p = arr[:]
            ans =[]
            for i in range(n):
                mz[i][p[i]]="Q"
                ans.append("".join(mz[i]))
            self.ans.append(ans)
        else:
            c = self.construct_candidates(arr,k,n)
            for i in range(len(c)):
                arr[k]=c[i]
                self.bt(arr, k+1, n)

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        if n ==0:
            return [[]]
        if n==1:
            return [["Q"]]

        arr = [0]*n
        self.bt(arr,0,n)
        return self.ans

if __name__ == "__main__":
    s = Solution()
    print(s.solveNQueens(4))