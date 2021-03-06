# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        if t1 is None and t2 is None:
            return None

        if t1 is None and t2 is not None:
            root = TreeNode(t2.val)
            root.left = self.mergeTrees(None, t2.left)
            root.right = self.mergeTrees(None, t2.right)
        elif t1 is not None and t2 is None:
            root = TreeNode(t1.val)
            root.left = self.mergeTrees(t1.left, None)
            root.right = self.mergeTrees(t1.right, None)

        else:
            root= TreeNode(t1.val + t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)

        return root
