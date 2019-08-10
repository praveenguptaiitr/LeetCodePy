class Solution:
    def minimumTotal(self, triangle):
        n = len(triangle)

        dp = [[float("inf")] * n for _ in range(n)]
        dp[0][0] = triangle[0][0]

        for i in range(1, n):
            for j in range(i + 1):
                dp[i][j] = triangle[i][j] + min(dp[i - 1][j], dp[i - 1][j - 1])

        return min(dp[n - 1])

if __name__ == "__main__":
    s = Solution()
    print(s.minimumTotal([[-1],[3,2],[1,-2, -1]]))
    print(s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))