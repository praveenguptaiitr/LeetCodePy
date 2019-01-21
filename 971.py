# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.i = 0
        self.ans = []

    def dfs(self, root, voyage):
        if root is None:
            return

        if root.val != voyage[self.i]:
            self.ans = [-1]
            return

        self.i += 1
        if (self.i < len(voyage) and root.left is not None and root.left.val != voyage[self.i]):
            self.ans.append(root.val)
            self.dfs(root.right, voyage)
            self.dfs(root.left, voyage)
        else:
            self.dfs(root.left, voyage)
            self.dfs(root.right, voyage)

    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """

        if root is None:
            return [-1]
        if len(voyage) == 0:
            return [-1]
        self.dfs(root, voyage)
        return self.ans