# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.maxLevel = 0
        self.maxVal = 0
    def traverse(self, root, depth):
        if root is None:
            return
        if depth > self.maxLevel:
            self.maxLevel = depth
            self.maxVal = root.val
        self.traverse(root.left, depth+1)
        self.traverse(root.right, depth + 1)
        return

    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return
        self.maxLevel = 0
        self.maxVal = root.val
        #depth = 0
        self.traverse(root,0)
        return self.maxVal