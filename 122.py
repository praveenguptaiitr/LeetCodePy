class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""

		if len(prices)==0:
			return 0
		peak = prices[0]
		valley = prices[0]
		profit = 0
		i=0
		while (i < len(prices)-1):
			while(i< len(prices)-1 and prices[i]>=prices[i+1]):
				i+=1
			valley=prices[i]

			while(i< len(prices)-1 and prices[i]<=prices[i+1]):
				i+=1
			peak=prices[i]


			profit+=peak-valley

		return profit


if __name__=="__main__":
	nums = [7,1,5,3,6,4]
	s = Solution()
	print(s.maxProfit([7,1,5,3,6,4]))