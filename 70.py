class Solution:
	def __init__(self):
		self.tbl = []

	def fib(self, n):
		if n == 0 or n == 1:
			return 1
		if self.tbl[n] != -1:
			return self.tbl[n]

		self.tbl[n] = self.fib(n - 1) + self.fib(n - 2)
		return self.tbl[n]

	def climbStairs(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		self.tbl = [-1] * (n + 1)
		return self.fib(n)
