# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.sum = 0

    def dfs(self, root, tillNow):
        if root is None:
            return

        self.dfs(root.left, tillNow*10+root.val)
        if root.left is None and root.right is None:
            self.sum +=(tillNow*10)+root.val
        self.dfs(root.right, tillNow * 10 + root.val)

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.dfs(root,0)

        return self.sum

if __name__=="__main__":
    s = Solution()
    t = TreeNode(4)
    t.left = TreeNode(9)
    t.right = TreeNode(0)
    t.left.left = TreeNode(5)
    t.left.right = TreeNode(1)
    print(s.sumNumbers(t))