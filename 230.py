# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.count=0
        self.kth = -1
    def helper(self,root,k):
        if root is None:
            return
        if root.left is not None:
            self.helper(root.left,k)
        self.count+=1
        if self.count == k:
            self.kth=root.val
        if root.right is not None:
            self.helper(root.right,k)
        return

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.helper(root,k)
        return self.kth