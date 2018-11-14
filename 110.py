# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def __init__(self):
		self.ans = True

	def isBalanced(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		if root is None:
			return True
		else:
			self.height(root)
		return self.ans

	def height(self, root):
		if root is None:
			return 0

		l = self.height(root.left)
		r = self.height(root.right)

		if (abs(l - r) > 1):
			self.ans= False

		return max(l, r) + 1