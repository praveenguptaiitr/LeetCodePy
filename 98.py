# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isbst(self, root, low, high):
        if root is None:
            return True

        if root.val <= low:
            return False
        if root.val >= high:
            return False

        l = True
        r = True

        if root.left is not None:
            if root.left.val < root.val:
                l = True
            else:
                l = False

        if root.right is not None:
            if root.right.val > root.val:
                r = True
            else:
                r = False

        return (l and r and self.isbst(root.left, low, root.val) and self.isbst(root.right, root.val, high))



    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root is None:
            return True


        return self.isbst(root, float("-inf"), float("inf"))