class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        tbl = [float("inf")]*(amount+1)
        tbl[0]=0
        for i in range(1, amount+1):
            for j in coins:
                if i-j >=0 and tbl[i-j]+1 < tbl[i]:
                    tbl[i]= tbl[i-j]+1

        if tbl[amount]!= float("inf"):
            return tbl[amount]
        else:
            return -1

if __name__ == "__main__":
    s = Solution()
    print(s.coinChange([1, 2, 5], 11))
    print(s.coinChange([ 2], 3))