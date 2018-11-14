# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def __init__(self):
		self.diameter = 0

	def diameterOfBinaryTree(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if root is None:
			return 0

		self.height(root)
		return self.diameter - 1

	def height(self, root):
		if root is None:
			return 0

		l = self.height(root.left)
		r = self.height(root.right)

		self.diameter = max(self.diameter, l + r + 1)
		return max(l, r) + 1

