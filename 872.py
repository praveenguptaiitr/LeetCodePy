# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.l1 = []
        self.l2 = []

    def traverse(self, root, l):
        if root is None:
            return

        if root.left is None and root.right is None:
            l.append(root.val)
        else:
            self.traverse(root.left, l)
            self.traverse(root.right, l)

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if root1 is None and root2 is None:
            return True
        if root1 is not None and root2 is None:
            return False
        if root1 is None and root2 is not None:
            return False

        self.traverse(root1, self.l1)
        self.traverse(root2, self.l2)
        return self.l1 == self.l2