# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = {}

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """

        if root is None:
            return False

        self.ans[root.val] = self.ans.get(root.val, 0) + 1

        if root.val == k - root.val:
            return self.findTarget(root.left, k) or (self.ans.get(k - root.val, -1) > 1) \
                   or self.findTarget(root.right, k)

        else:
            return self.findTarget(root.left, k) or (self.ans.get(k - root.val, -1) > 0) \
                   or self.findTarget(root.right, k)



