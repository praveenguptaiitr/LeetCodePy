# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def dfs(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        if root is None:
            return None

        l = self.dfs(root.left)
        r = self.dfs(root.right)
        if l is not None:
            root.right = l
            while(l.right is not None):
                l = l.right
            l.right = r
        root.left = None
        return root

    def flatten(self, root):
        root = self.dfs(root)

if __name__== "__main__":
    s = Solution()
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.left.left = TreeNode(3)
    t.left.right = TreeNode(4)
    t.right = TreeNode(5)
    t.right.right = TreeNode(6)
    s.flatten(t)
    print(t)
    x = t
    print("-"*10)
    while ( x is not None):
        print(x.val)
        x = x.right