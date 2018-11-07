# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.l = []

    def dfs(self, root, v):
        if root is None:
            return
        v.append(root.val)
        if root.left is None and root.right is None:
            self.l.append("->".join(str(i) for i in v))
            return
        else:
            if root.left is not None:
                self.dfs(root.left,v)
            if root.right is not None:
                self.dfs(root.right,v)
        v.pop()
        return


    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return
        v = []
        self.dfs(root,v)
        return self.l