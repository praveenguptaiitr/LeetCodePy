# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if root is None:
            return None
        if root == p:
            return root

        if root == q:
            return root

        l1 = None
        l2 = None
        if root.left is not None:
            l1 = self.lowestCommonAncestor(root.left, p, q)
        if root.right is not None:
            l2 = self.lowestCommonAncestor(root.right, p, q)


        if l1 is not None and l2 is not None:
            return root

        elif l1 is not None and l2 is None:
            return l1

        else: #l2 is not None and l1 is None:
            return l2


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if root is None:
            return None
        if root == p:
            return root

        if root == q:
            return root

        l1 = self.lowestCommonAncestor(root.left, p, q)
        l2 = self.lowestCommonAncestor(root.right, p, q)

        if l1 is not None and l2 is not None:
            return root

        if l1 is not None and l2 is None:
            return l1
        if l1 is None and l2 is not None:
            return l2

        return None

