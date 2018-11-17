# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
	def __init__(self):
		self.ans = ""

	def dfs(self, root):
		if root is None:
			return ""
		if root.left is None and root.right is None:
			self.ans += str(root.val)
			return

		self.ans += str(root.val)
		if root.left is None:
			self.ans += "()"
		else:
			self.ans+="("
			self.dfs(root.left)
			self.ans += ")"

		if root.right is not None:
			self.ans += "("
			self.dfs(root.right)
			self.ans += ")"

	def tree2str(self, t):
		"""
		:type t: TreeNode
		:rtype: str
		"""

		self.dfs(t)
		return self.ans


if __name__ == "__main__":
	s = Solution()
	t = TreeNode(1)
	t.left = TreeNode(2)
	t.left.left = TreeNode(4)
	t.right = TreeNode(3)
	print(s.tree2str(t))