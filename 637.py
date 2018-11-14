# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	def averageOfLevels(self, root):
		"""
		:type root: TreeNode
		:rtype: List[float]
		"""
		if root is None:
			return []
		ans = []
		q = []
		q.append(root)
		next = []
		ans.append(root.val)
		while (len(q) > 0):
			for e in q:
				if e.left is not None:
					next.append(e.left)
				if e.right is not None:
					next.append(e.right)
			if len(next)>0:
				s = sum([x.val for x in next])
				ans.append(s / len(next))
				q = next
				next = []
			else:
				break


		return ans



if __name__ == "__main__":
	s = Solution()
	t = TreeNode(2)
	t.left = TreeNode(8)
	t.right = TreeNode(10)
	t.left.left = TreeNode(15)
	t.left.right = TreeNode(7)
	s.averageOfLevels(t)