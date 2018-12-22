# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.ans = 0

    def dfs(self, root,L, R):
        if root is None:
            return 0

        self.dfs(root.left, L,R)
        if root.val >= L and root.val <= R:
            self.ans+=root.val

        self.dfs(root.right, L, R)


    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """

        self.dfs(root, L, R)
        return self.ans

if __name__ == "__main__":
    s = Solution()
    t = TreeNode(5)
    t.left = TreeNode(3)
    t.left.right = TreeNode(4)
    t.right = TreeNode(20)
    t.right.right = TreeNode(25)
    print(s.rangeSumBST(t,4,20))
