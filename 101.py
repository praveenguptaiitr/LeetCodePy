# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def mirror(self, root1, root2):
        if root1 is None and root2 is None:
            return True

        if root1 is None and root2 is not None:
            return False

        if root2 is None and root1 is not None:
            return False

        if self.mirror(root1.left, root2.right) and self.mirror(root1.right,root2.left) \
            and root1.val == root2.val:
            return True
        else:
            return False




    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.mirror(root,root)
