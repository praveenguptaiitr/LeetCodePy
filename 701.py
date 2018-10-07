# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            t = TreeNode(val)
            root = t
            return root

        t = TreeNode(val)
        temp = root
        prev = None
        while(temp is not None):
            prev = temp
            if temp.val<val:
                temp = temp.left
            else:
                temp = temp.right

        if prev.val<val:
            prev.left = t
        else:
            prev.right = t

        return root