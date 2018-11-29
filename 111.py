# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        l1 = self.minDepth(root.left)
        l2 = self.minDepth(root.right)
        if l1 == 0 and l2 != 0:
            return l2 + 1
        if l1 != 0 and l2 == 0:
            return l1 + 1

        return 1 + min(l1, l2)
