# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.ans = 0

    def dfs(self, root):
        if root is None:
            return 0

        l = self.dfs(root.left)
        r = self.dfs(root.right)
        al = 0
        ar = 0
        if root.left != None and root.val == root.left.val:
            al = l+1
        if root.right != None and root.val == root.right.val:
            ar = r+1

        self.ans = max(self.ans,al+ar)
        return max(al,ar)

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0

        self.dfs(root)
        return self.ans


if __name__ == "__main__":
    s = Solution()
    t = TreeNode(1)
    t.left = TreeNode(1)
    t.right = TreeNode(1)

    print(s.longestUnivaluePath(t))