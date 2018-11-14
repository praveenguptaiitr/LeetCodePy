# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def isBalanced(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		if root is None:
			return True
		else:
			return self.height(root) != -1

	def height(self, root):
		if root is None:
			return 0
		l = self.height(root.left)
		if l == -1:
			return -1
		r = self.height(root.right)
		if r == -1:
			return -1

		if (abs(l - r) > 1):
			return -1
		else:
			return max(l, r) + 1