class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        tbl = [0] * (amount + 1)
        tbl[0] = 1

        for i in range(len(coins)):
            for j in range(1, amount + 1):
                if j - coins[i] >= 0:
                    tbl[j] += tbl[j - coins[i]]

        return tbl[amount]


if __name__ == "__main__":
    s = Solution()
    print(s.change(5,[1,2,5]))
